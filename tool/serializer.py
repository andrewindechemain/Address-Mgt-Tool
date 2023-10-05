"""This file contains serialized models that will be used for API View
."""
from rest_framework import serializers
from .models import *

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields= '__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=Address
        fields= '__all__'
