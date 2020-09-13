from  django.db import models
from django.contrib.auth.models import User

class CustomarRegistration(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    password = models.CharField(max_length=500)

    def __str__(self):
        return self.email

    def register(self):
        self.save()

    def isExist(self):
        if CustomarRegistration.objects.filter(email=self.email):
           return True
        return False

    @staticmethod
    def get_customer_by_email(email):
        try:
            return CustomarRegistration.objects.get(email=email)
        except:
            return False