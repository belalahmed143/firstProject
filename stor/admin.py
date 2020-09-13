from django.contrib import admin
from  .models.product import Product
from  .models.category import Category
from  .models.customer import CustomarRegistration
from .models.order import CustomerOrders
# Register your models here.
class AdminProduct(admin.ModelAdmin):
    list_display=['product_name','id','price']

# class AdminCustomar(admin.ModelAdmin):
#     list_display=['username','email']

admin.site.register(Product,AdminProduct)
admin.site.register(Category)
admin.site.register(CustomarRegistration)
admin.site.register(CustomerOrders)
