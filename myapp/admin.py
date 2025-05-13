from django.contrib import admin
from .models import Category, Product, Subscriber, Order

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "preview_background", "preview_image")
    readonly_fields = ("preview_background", "preview_image")
    fields = ("name", "description", "background_image", "preview_background", "category_image", "preview_image", "banner_image")

    def preview_background(self, obj):
        if obj.background_image:
            return f'<img src="{obj.background_image.url}" style="height: 100px;" />'
        return "-"
    preview_background.allow_tags = True
    preview_background.short_description = "Превʼю фону"

    def preview_image(self, obj):
        if obj.category_image:
            return f'<img src="{obj.category_image.url}" style="height: 100px;" />'
        return "-"
    preview_image.allow_tags = True
    preview_image.short_description = "Превʼю іконки"

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "available", "stock", "created_at")
    list_filter = ("category", "available")
    search_fields = ("name", "category__name")

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ("email", "subscribed_at")
    search_fields = ("email",)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'payment_method', 'total_price', 'created_at']
    search_fields = ['first_name', 'last_name', 'phone']
    list_filter = ['payment_method', 'delivery_method', 'created_at']
    readonly_fields = ['products_display', 'total_price', 'delivery_method', 'promo_code']

    def get_fields(self, request, obj=None):
        fields = ['first_name', 'last_name', 'phone', 'delivery_method']

        if obj:
            if obj.delivery_method == "ukr_poshta":
                fields += ['city_ukrposhta', 'street_ukrposhta', 'postal_code']
            elif obj.delivery_method == "nova_poshta":
                fields += ['city_nova_poshta', 'street_nova_poshta', 'nova_poshta_branch']

        fields += ['payment_method', 'promo_code', 'products_display', 'total_price']
        return fields

    def products_display(self, obj):
        from django.utils.safestring import mark_safe

        try:
            products = obj.products_json
        except Exception:
            return "Неможливо прочитати список товарів"

        result = "<ul>"
        for p in products:
            name = p.get('name', '')
            price = p.get('price', '')
            quantity = p.get('quantity', '')
            result += f"<li><b>{name}</b> — {price} грн × {quantity}</li>"
        result += "</ul>"

        return mark_safe(result)

    def total_price(self, obj):
        # Функція для відображення суми замовлення
        return f"{obj.total_price} грн"

    products_display.short_description = "Список товарів"
    total_price.short_description = "Загальна сума"
