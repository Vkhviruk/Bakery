from django.shortcuts import render, redirect
from myapp.models import Category, Product, Subscriber
from myapp.forms import SubscriberForm
from django.contrib import messages

def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    form = SubscriberForm()
    return render(request, 'myapp/home.html', {
        'categories': categories,
        'products': products,
        'form': form
    })

def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Дякуємо за підписку!")
    return redirect('home')

def category_detail(request, category_id):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'myapp/category_detail.html', {
        'category': category,
        'products': products,
    })

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'myapp/product_detail.html', {
        'product': product,
    })
