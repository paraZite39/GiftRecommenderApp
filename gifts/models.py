from django.db import models

class Product(models.Model):
    product_title = models.CharField(max_length=50)
    product_subtitle = models.CharField(max_length=200)
    product_picture = models.ImageField()
    product_link = models.URLField(max_length=200)
