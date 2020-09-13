from django import forms
from django.forms import ModelForm
from  .models.customer import CustomarRegistration
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Customer_Ragistration(UserCreationForm):
    full_name =forms.CharField(max_length=20,widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Enter Yorr full name "
    })) 
    username = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={
            "class":"form-control",
            "placeholder":"Enter your username.."
        }) 
        )
    email = forms.EmailField(
            widget=forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"Enter your email.."
            }) 
            )
    password1 = forms.CharField(
            widget=forms.PasswordInput(attrs={
                "class":"form-control",
                "placeholder":"Enter your password.."
            }) 
            )
    password2 = forms.CharField(max_length=30,
            widget=forms.PasswordInput(attrs={
                "class":"form-control",
                "placeholder":"Confirme password.."
            }) 
            )   
    class Meta:
        model=User
        fields =['full_name', 'username', 'email', 'password1','password2']

