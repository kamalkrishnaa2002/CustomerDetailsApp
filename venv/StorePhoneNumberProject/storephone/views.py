
from .models import Store, Category
from .forms import StoreForm, CategoryForm
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Store



def store_form(request):

    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('store_list')
    else:
        form = StoreForm()
    
    context = {'form': form}
    return render(request, 'storephone/store_form.html', context)



def store_list_view(request):
    categories = Category.objects.all()
    selected_category = request.GET.get('category')

    if selected_category:
        stores = Store.objects.filter(category_id=selected_category, button_clicked=False)
    else:
        stores = Store.objects.all()

    for store in stores:
        if store.button_clicked:
            store.phone_number = ''  # Remove phone number if button clicked

    context = {
        'stores': stores,
        'categories': categories,
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
    store = get_object_or_404(Store, pk=store_id)
    if request.method == 'POST':
        store.button_clicked = True
        store.save()
    return redirect('store_list')  # Replace 'store_list' with the name of your store list view