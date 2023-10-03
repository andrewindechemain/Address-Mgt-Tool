from django.db import models
import ipaddress

# Create your models here.
class Users(models.Model):
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=50)

class Customer(models.Model): 
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)