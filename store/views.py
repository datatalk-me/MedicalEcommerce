from django.shortcuts import render,get_object_or_404
from .models import Product
from category.models import Category
# Create your views here.



def store(request,category_slug=None):

    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category,category_slug=category_slug)
        products = Product.objects.filter(product_category=categories,product_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(product_available=True)
        product_count = products.count()

    data = {
        'products': products,
        'product_count': product_count

    }
    return render(request,'store/store.html',data)


def product_detail(request,category_slug,product_slug):
    try:
        single_product = Product.objects.get(product_category__category_slug=category_slug,product_slug=product_slug)
    except Exception as e:
        raise e
    data = {
        'single_product': single_product
    }
    return render(request,'store/product_detail.html',data)