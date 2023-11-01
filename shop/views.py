from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def product_list(request, category_slug=None):
    #it will holds the category from the url if it exists
    category = None
    categories = Category.objects.all()
    products= Product.objects.filter(available= True)
    #if there a category_slug exists in the request
    if category_slug:
        #bring the category from db that its slug equals to category_slug
        category = get_object_or_404(Category, slug = category_slug)
        # filter the products with this category
        products = Product.objects.filter(category=category)
    return render(request, 'shop/product/list.html', {'category':category, 'categories':categories, 'products':products})

def product_detail(request, id , slug):
    product = get_object_or_404(Product, id=id, slug=slug, available= True)
    return render(request, 'shop/product/detail.html', {'product', product})