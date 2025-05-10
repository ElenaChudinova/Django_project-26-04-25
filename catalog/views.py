from django.shortcuts import render, get_object_or_404, redirect
from catalog.models import Product
from .forms import ProductForm

def index(request):
    return render(request, 'products_list.html')

def products_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products_list.html', context)


def info_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, "info_product.html", context=context)


def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalog:product_list')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})
