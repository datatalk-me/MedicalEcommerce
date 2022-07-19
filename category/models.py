from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100,unique=True)
    category_slug = models.SlugField(max_length=100, unique=True)
    category_description = models.TextField(max_length=500, blank=True)
    category_image = models.ImageField(upload_to='photos/category/', blank=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['category_name']

    def get_url(self):
        return reverse('products_by_category', kwargs={'category_slug': self.category_slug})

    def __str__(self):
        return self.category_name