from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def home(request):
    data = Product.objects.all()
    context = {'product': data}
    return render(request, "base_list.html", context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, "product_detail.html", context)
