from django.db import models
from .category import Category
from django.contrib.auth.models import User

# Create your models here

class Product(models.Model):
    product_code = models.IntegerField()
    product_name = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE, default=1)
    descriptionn =models.CharField(max_length=200)
    product_img = models.ImageField(default='no_image.jpg',upload_to='Product_Image')

    def __str__(self):
        return self.product_name

    @staticmethod
    def products_category(categoryid):
        if categoryid:
            return Product.objects.filter(category=categoryid)
        else:
            return Product.objects.all()
    @staticmethod
    def product_get_id(ids):
        return Product.objects.filter(id__in=ids)