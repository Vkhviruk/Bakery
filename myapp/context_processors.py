# myapp/context_processors.py
from .models import Product

def all_products(request):
    return {
        'all_products': Product.objects.all()
    }
