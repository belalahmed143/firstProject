from django.shortcuts import render,redirect,HttpResponse
from stor.models.customer import CustomarRegistration
from stor.forms import Customer_Ragistration
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.views import View



class Login(View):
    def get(self,request):
        return render(request,'signin.html')
    def post(self, request):
        email=request.POST.get('email')
        password=request.POST.get('password')
        customer= CustomarRegistration.get_customer_by_email(email)
        error_messages = None

        if customer: 
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] =customer.id
                messages.success(request, f'Login Success, Welcome to Home page')
                return redirect('index')
            else:
                error_messages=('email or password incorrect')
        else:
           error_messages=('email or password incorrect')        
        context ={
            'error':error_messages
            }
        return render(request,'signin.html',context)

# def signin(request):
#     if request.method == 'GET':
#           return render(request,'signin.html')
#     else:
#         email=request.POST.get('email')
#         password=request.POST.get('password')
#         customer= CustomarRegistration.get_customer_by_email(email)
#         error_messages = None

#         if customer:
#             flag = check_password(password, customer.password)
#             if flag:
#                 return redirect('index')
#             else:
#                 error_messages=('email or password incorrect')
#         else:
#            error_messages=('email or password incorrect')        
#         context ={
#             'error':error_messages
#             }
#         return render(request,'signin.html',context)