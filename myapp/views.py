from django.http import JsonResponse
from django.shortcuts import render, redirect
from myapp.models import Category, Product, Subscriber, Order
from myapp.forms import SubscriberForm
from django.contrib import messages
from decimal import Decimal, InvalidOperation
import json

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

def checkout(request):
    return render(request, 'myapp/checkout.html')


def process_order(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        delivery_method = request.POST.get('delivery_method')
        payment_method = request.POST.get('payment_method')
        promo_code = request.POST.get('promo_code')

        order_items = json.loads(request.POST.get('order_items', '[]'))

        order_total = sum([Decimal(item['price']) * item['quantity'] for item in order_items])

        order_data = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'delivery_method': delivery_method,
            'payment_method': payment_method,
            'promo_code': promo_code,
            'products_json': order_items,
            'total_price': order_total,
        }

        if delivery_method == "ukr_poshta":
            order_data.update({
                'city_ukrposhta': request.POST.get('ukrposhta_city'),
                'street_ukrposhta': request.POST.get('ukrposhta_street'),
                'postal_code': request.POST.get('ukrposhta_postal_code'),
            })

        elif delivery_method == "nova_poshta":
            order_data.update({
                'city_nova_poshta': request.POST.get('nova_city'),
                'street_nova_poshta': request.POST.get('nova_street'),
                'nova_poshta_branch': request.POST.get('nova_poshta_branch'),
            })

        Order.objects.create(**order_data)

        return redirect('success_page')

    return JsonResponse({'error': 'Invalid request'}, status=400)

def success_page(request):
    return render(request, 'success.html')
