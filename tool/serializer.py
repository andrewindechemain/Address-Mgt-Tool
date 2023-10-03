from .models import *
from rest_framework import serializers

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=["name","email"]

class IPAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=IPAddress
        fields=["ip","customer","allocated"]