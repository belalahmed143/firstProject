from django.db import models
from django.contrib.auth.models import User
from stor.models.product import Product
from stor.models.customer import CustomarRegistration
import datetime

# Create your models here.


class CustomerOrders(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer = models.ForeignKey(CustomarRegistration, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.IntegerField()
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=14)
    date = models.DateTimeField(default=datetime.datetime.today)

