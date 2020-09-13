from django.shortcuts import render,redirect,HttpResponse
from stor.models.customer import CustomarRegistration
from  stor.forms import Customer_Ragistration
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import  login
from django.views import View


class Registration(View):
    def get(self,request):
        return render(request, 'signup.html')
    def post(self, request):
        postData = request.POST
        first_name =postData.get('firstname')
        last_name =postData.get('lastname')
        email =postData.get('email')
        mobile_number =postData.get('phone')
        password =postData.get('password')

        value ={
            'first_name':first_name,
            'last_name':last_name,
            'email': email,
            'mobile_number' : mobile_number,
        }
        error_messages = None
        customarregistration = CustomarRegistration(
            first_name=first_name,
            last_name=last_name,
            email= email,
            mobile_number = mobile_number,
            password=password
        )

        if len(password) < 6:
            error_messages = 'password must be 6 char long'
        elif customarregistration.isExist():
            error_messages = 'Email already exixt'
        if not error_messages:
            customarregistration.password = make_password(customarregistration.password)
            customarregistration.register()
            return redirect('signin')
        else:
            context ={
                'error':error_messages,
                'value':value
            }
            return render(request, 'signup.html', context)


# def signup(request):
#     if request.method == 'GET':       
#         return render(request, 'signup.html')
#     else:
#         postData = request.POST
#         first_name =postData.get('firstname')
#         last_name =postData.get('lastname')
#         email =postData.get('email')
#         mobile_number =postData.get('phone')
#         password =postData.get('password')

#         value ={
#             'first_name':first_name,
#             'last_name':last_name,
#             'email': email,
#             'mobile_number' : mobile_number,
#         }
#         error_messages = None
#         customarregistration = CustomarRegistration(
#             first_name=first_name,
#             last_name=last_name,
#             email= email,
#             mobile_number = mobile_number,
#             password=password
#         )

#         if len(password) < 6:
#             error_messages = 'password must be 6 char long'
#         elif customarregistration.isExist():
#             error_messages = 'Email already exixt'
#         if not error_messages:
#             customarregistration.password = make_password(customarregistration.password)
#             customarregistration.register()
#             return redirect('signin')
#         else:
#             context ={
#                 'error':error_messages,
#                 'value':value
#             }
#             return render(request, 'signup.html', context)