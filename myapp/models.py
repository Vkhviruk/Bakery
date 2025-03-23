from django.db import models

# Модель категорії
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Назва категорії")
    description = models.TextField(blank=True, verbose_name="Опис")

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
    ]

    name = models.CharField(max_length=255, verbose_name="Назва продукту")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категорія")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Ціна")
    stock = models.PositiveIntegerField(default=10, verbose_name="Кількість на складі")
    description = models.TextField(blank=True, verbose_name="Опис")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата оновлення")
    available = models.BooleanField(default=True, verbose_name="В наявності")
    product_type = models.CharField(
        max_length=10, choices=CATEGORY_CHOICES, default="bread", verbose_name="Тип продукту"
    )

    def __str__(self):
        return f"{self.name} - {self.price} грн"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукти"
