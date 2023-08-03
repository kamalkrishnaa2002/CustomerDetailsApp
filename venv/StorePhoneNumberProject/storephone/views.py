
from .models import Store, Category
from .forms import StoreForm, CategoryForm
from django.shortcuts import render, redirect



def store_form(request):
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            category_id = request.POST['category']
            if category_id:
                category = Category.objects.get(id=category_id)
                store = form.save(commit=False)
                store.category = category
                store.save()
                return redirect('store_form')
    else:
        form = StoreForm()
    categories = Category.objects.all()
    return render(request, 'storephone/store_form.html', {'form': form, 'categories': categories})


def store_list_view(request):
    categories = Category.objects.all()
    selected_category = request.GET.get('category')

    if selected_category:
        stores = Store.objects.filter(category_id=selected_category)
    else:
        stores = Store.objects.all()

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