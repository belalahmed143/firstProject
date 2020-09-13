from django.shortcuts import render,redirect,HttpResponse
from  stor.models.product import Product
from  stor.models.category import Category
from  stor.models.customer import CustomarRegistration
from  stor.forms import Customer_Ragistration
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import  login
from django.views import View
# Create your views here.
class Index(View):
    def get(self,request):
        products = None
        categories = Category.objects.all()
        categoryId = request.GET.get('category')
        if categoryId:
            products =Product.products_category(categoryId)
        else:
            products =Product.objects.all()
        context = {
            'products':products,
            'categories':categories 
        }
        print('You are :', request.session.get('email'))
        return render(request, 'index.html', context)

    def post(self,request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        print(product)
        cart=request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                else:
                    cart[product] = quantity+1
            else:           
                cart[product] = 1
        else:
            cart ={}
            cart[product] = 1
        request.session['cart'] = cart
        print ("cart :",request.session['cart'])
        return redirect('/')
