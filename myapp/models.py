from django.db import models

# Модель категорії
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Назва категорії")
    description = models.TextField(blank=True, verbose_name="Опис")
    background_image = models.ImageField(upload_to='category_backgrounds/', verbose_name="Фонове зображення (дошка)", blank=True, null=True)
    category_image = models.ImageField(upload_to='category_images/', verbose_name="Зображення продукту", blank=True, null=True)
    banner_image = models.ImageField(upload_to='categories/banners/', verbose_name="Зображення банера", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

# Модель продукту
class Product(models.Model):
    CATEGORY_CHOICES = [
        ("bread", "Хліб"),
        ("cake", "Торт"),
        ("cookie", "Печиво"),
        ("drink", "Напій"),
        ("semi-finished product", "Напівфабрикат"),
    ]

    name = models.CharField(max_length=255, verbose_name="Назва продукту")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категорія")
    price = models.DecimalField(max_digits=6, decimal_places=0, verbose_name="Ціна")
    stock = models.PositiveIntegerField(default=10, verbose_name="Кількість на складі")
    description = models.TextField(blank=True, verbose_name="Опис")
    ingredients = models.TextField(blank=True, verbose_name="Cклад")
    weight = models.PositiveIntegerField(default=100, verbose_name="Вага")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата оновлення")
    available = models.BooleanField(default=True, verbose_name="В наявності")
    product_type = models.CharField(
        max_length=30, choices=CATEGORY_CHOICES, default="bread", verbose_name="Тип продукту"
    )

    product_image = models.ImageField(upload_to='product_images/', blank=True, null=True, verbose_name="Зображення продукту")

    def __str__(self):
        return f"{self.name} - {self.price} грн"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукти"

class Subscriber(models.Model):
    email = models.EmailField(unique=True, verbose_name="Емейл")
    subscribed_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата підписки")

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Підписник"
        verbose_name_plural = "Підписники"


class Order(models.Model):
    PAYMENT_CHOICES = [
        ('google_pay', 'Google Pay'),
        ('apple_pay', 'Apple Pay'),
        ('cod', 'Післяплата'),
    ]
    DELIVERY_CHOICES = [
        ('nova_poshta', 'Нова Пошта'),
        ('ukr_poshta', 'Укрпошта'),
    ]

    first_name = models.CharField(max_length=100, verbose_name="Ім'я клієнта")
    last_name = models.CharField(max_length=100, verbose_name="Призвіще клієнта")
    phone = models.CharField(max_length=20, verbose_name="Номер телефону клієнта")

    delivery_method = models.CharField(max_length=20, choices=DELIVERY_CHOICES, verbose_name="Спосіб доставки")
    # Поля для Укрпошти
    city_ukrposhta = models.CharField(max_length=255, blank=True, null=True, verbose_name="Місто")
    street_ukrposhta = models.CharField(max_length=255, blank=True, null=True, verbose_name="Вулиця")
    postal_code = models.CharField(max_length=20, blank=True, null=True, verbose_name="Поштовий індекс")

    # Поля для Нової Пошти
    city_nova_poshta = models.CharField(max_length=255, blank=True, null=True, verbose_name="Місто")
    street_nova_poshta = models.CharField(max_length=255, blank=True, null=True, verbose_name="Вулиця")
    nova_poshta_branch = models.CharField(max_length=20, blank=True, null=True, verbose_name="Номер відділення / поштомату")

    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES, verbose_name="Спосіб оплати")
    promo_code = models.CharField(max_length=50, blank=True, null=True, verbose_name="Промокод")

    products_json = models.JSONField(blank=True, null=True, verbose_name="Товари (JSON)")  # нове поле
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Загальна сума")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")

    def get_full_address(self):
        if self.delivery_method == 'ukr_poshta':
            return f"{self.city_ukrposhta}, {self.street_ukrposhta}, {self.postal_code}"
        elif self.delivery_method == 'nova_poshta':
            return f"{self.city_nova_poshta}, {self.street_nova_poshta}, Відділення: {self.nova_poshta_branch}"
        return "Адреса не вказана"

    get_full_address.short_description = 'Адреса доставки'

    def delivery_method_display(self, obj):
        return obj.delivery_method
    delivery_method_display.short_description = "Спосіб доставки"

    def __str__(self):
        return f"{self.first_name} {self.last_name} — {self.total_price} грн"

    class Meta:
        verbose_name = "Замовлення"
        verbose_name_plural = "Замовлення"
