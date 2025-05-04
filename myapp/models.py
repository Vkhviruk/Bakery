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
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Ціна")
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
