from django.shortcuts import render, get_object_or_404
from catalog.models import Product


def base(request):
    data = Product.objects.all()
    context = {'product': data}
    return render(request, "home-1.html", context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, "product_detail.html", context)


def contact(request):
    context = 'contact.html'
    return render(request, context)
