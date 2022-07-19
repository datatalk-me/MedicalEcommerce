from django.db import models
from category.models import Category
from django.urls import reverse
# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_slug = models.SlugField(max_length=255)
    product_description = models.TextField(blank=True)
    product_price = models.DecimalField(max_digits=6, decimal_places=2)
    product_image = models.ImageField(upload_to='images/', blank=True)
    product_stock = models.IntegerField(default=0)
    product_available = models.BooleanField(default=True)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_created_date = models.DateTimeField(auto_now_add=True)
    product_updated_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_detail', kwargs={'category_slug': self.product_category.category_slug, 'product_slug': self.product_slug})

    def __str__(self):
        return self.product_name