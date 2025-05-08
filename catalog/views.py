from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from catalog.models import Product

def index(request):
    return render(request, 'products_list.html')

def products_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products_list.html', context)


def info_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, "info_product.html", context=context)

def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")

        return HttpResponse(f"Спасибо, {name}. Сообщение получено.")
    return render(request, 'catalog/contacts.html')
