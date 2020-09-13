from django.shortcuts import render,redirect
from django.views import View
from stor.models.product import Product

class Cart(View):
    def get(self, request):
        ids=list(request.session.get('cart').keys())
        carts=Product.product_get_id(ids)
        context={
           'carts':carts
        }
        print(carts)
        return render(request,'cart.html',context)