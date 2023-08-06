
from .models import Store, Category
from .forms import StoreForm, CategoryForm
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Store
from django.utils import timezone
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

def store_form(request):
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            store = form.save(commit=False)
            store.registered_date = timezone.now()  # Import timezone if not imported
            store.save()
            return redirect('store_list')
    else:
        form = StoreForm()

    context = {'form': form}
    return render(request, 'storephone/store_form.html', context)


def store_list_view(request):
    categories = Category.objects.all()
    selected_category = request.GET.get('category')
    selected_status = request.GET.get('status')

    stores = Store.objects.all()

    if selected_category:
        stores = stores.filter(category_id=selected_category)

    if selected_status == "clicked":
        stores = stores.filter(button_clicked=True)
        # Update clicked_at_date for clicked stores
        Store.objects.filter(pk__in=stores).update(clicked_at_date=timezone.now())
    elif selected_status == "unclicked":
        stores = stores.filter(button_clicked=False)

    context = {
        'stores': stores,
        'categories': categories,
        'selected_category': selected_category,
        'selected_status': selected_status,
    }

    return render(request, 'storephone/store_list.html', context)


def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('store_form')
    else:
        form = CategoryForm()
    return render(request, 'storephone/create_category.html', {'form': form})



def update_button_clicked(request, store_id):
    if request.method == 'POST':
        store = get_object_or_404(Store, pk=store_id)
        if not store.button_clicked:
            store.button_clicked = True
            store.clicked_at_date = timezone.now()
            store.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'already_clicked'})

    return JsonResponse({'status': 'invalid_method'})


def send_whatsapp(request, store_id):
    store = Store.objects.get(id=store_id)
    return redirect(f'https://api.whatsapp.com/send?phone={store.phone_number}')