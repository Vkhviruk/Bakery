from django import forms
from .models import Subscriber, Order

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'first_name', 'last_name', 'phone',
            'delivery_method',
            'city_ukrposhta', 'street_ukrposhta', 'postal_code',
            'city_nova_poshta', 'street_nova_poshta', 'nova_poshta_branch',
            'payment_method', 'promo_code', 'total_price'
        ]
