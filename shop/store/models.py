from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='categories/', null=True, blank=True)
    slug = models.SlugField(unique=True, null=True)
    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               null=True,
                               blank=True,
                               related_name='subcategories')
    
    def get_absolute_url(self):
        pass

    def __str__(self):
        return self.title
    
    def __repr__(self) :
        return f'Category: pk={self.pk}, title={self.title}'
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=0)
    description = models.TextField(default='Soon...')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    slug = models.SlugField(unique=True, null=True)
    size = models.IntegerField(default='30')
    color = models.CharField(max_length=40, default='Gold')

    def get_absolute_url(self):
        pass

    def __str__(self):
        return self.title
    
    def __repr__(self) :
        return f'Category: pk={self.pk}, title={self.title}, price={self.price}'
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Gallery(models.Model):
    image = models.ImageField(upload_to='products/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'