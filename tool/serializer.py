"""This file contains serialized models that will be used for API View
."""
from rest_framework import serializers
from .models import *

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=["name","email"]

class IPAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=IPAddress
        fields=["ip","customer","allocated"]
