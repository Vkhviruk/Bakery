from django.contrib import admin
from .models import Category, Product, Subscriber

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
