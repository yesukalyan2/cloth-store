from django.shortcuts import get_object_or_404, render
from .models import Category, Product


def product_list(request, category_slug=None):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    selected_category = None
    if category_slug:
        selected_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=selected_category)
    return render(request, "store/product_list.html", {"categories": categories, "products": products, "selected_category": selected_category})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    return render(request, "store/product_detail.html", {"product": product})
