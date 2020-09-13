from django.shortcuts import render,redirect
from django.views import View
from stor.models.product import Product
from stor.models.order import CustomerOrders
from stor.models.customer import CustomarRegistration


def cart_quantity(product,cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return 0


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.product_get_id(list(cart.keys()))
        print(address,phone,customer,cart,products)
        
        for product in products:
            order = CustomerOrders(
                customer = CustomarRegistration(id=customer),
                product=product,
                price=product.price,
                address=address,
                phone = phone,
                quantity =product.id
            )
            order.save()
        request.session['cart'] = {}
        return redirect('cart')
