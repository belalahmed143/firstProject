from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.views import View




def logout(request):
    request.session.clear()
    messages.success( request,'Successfully Logout')
    return redirect('signin')