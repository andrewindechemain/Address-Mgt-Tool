from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import ipaddress
from ipaddress import IPv4Network
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from .models import Address,Customer
from rest_framework import serializers
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User as AuthUser
from rest_framework.serializers import ModelSerializer
from rest_framework.views import APIView
from .serializers import AddressSerializer,CustomerSerializer,AllocatedIpsSerializer,IpAllocationSerializer
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from drf_yasg.generators import OpenAPISchemaGenerator


@permission_classes([IsAuthenticated]) 
@authentication_classes([BasicAuthentication]) 

class IpAllocationView(APIView):
    @login_required 
    def post(self, request, **kwargs):
        customer = kwargs.get("customer") 
        email = kwargs.get("email") 

        if not customer or not email:
            return Response({"error": "Please enter customer and email"}, status=status.HTTP_404_NOT_FOUND)
        customer = Customer.objects.filter(email=email).first()
        if not customer:
            customer = Customer(email=email)
            customer.save()
        existing_ip = Address.objects.filter(customer=customer, allocated=True).first() 
        if existing_ip:
            return Response({"error": "Customer already has an allocated IP"}, status=status.HTTP_400_BAD_REQUEST) 
        ip = Address.objects.filter(allocated=False).first()
        if not ip:
            return Response({"error": "No IPs available"}, status=status.HTTP_500_BAD_REQUEST)
        ip.customer = customer
        ip.allocated = True
        ip.save()

        serializer = AddressSerializer(ip)
        return Response('Successfully allocated IP',serializer.data, status=status.HTTP_200_OK)

class ReleaseIpView(APIView):
     def put(self, request, ipAddress):
        ip = get_object_or_404(Address, ip=ipAddress)
        if ip.allocated:
            ip.customer = None
            ip.allocated = False
            ip.save()
            serializer = AddressSerializer(ip) 
            return Response({'message': 'IP successfully released', 'ip': serializer.data}, status=status.HTTP_200_OK) # pass the serializer data here
        return Response('The typed IP has not been allocated', status=status.HTTP_404_NOT_FOUND)

class AllocatedIpsView(APIView):
    def get(self, request):
        ips = Address.objects.filter(allocated=True).select_related('customer')
        if ips:
            serializer = AllocatedIpsSerializer(ips, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response('No allocated IPs found.', status=status.HTTP_404_NOT_FOUND)
    
class AvailableIpsView(APIView):
    def get(self, request):
        ips = Address.objects.filter(allocated=False).values('ip', 'allocated')
        if ips:
            serializer = AddressSerializer(ips, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK) # remove the positional argument here
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED) # remove the positional argument here

class CustomSchemaGenerator(OpenAPISchemaGenerator):
    def get_endpoints(self, request):
        endpoints = super().get_endpoints(request)
        filtered_endpoints = {}
        for path, (method, view) in endpoints.items():
           if view.has_permission(request):
                filtered_endpoints[path] = (method, view)
        return filtered_endpoints
    
def subnet_calculations(ip, mask):
    network = ipaddress.IPv4Network(f"{ip}/{mask}", strict=False)
    return {
        "network_address": str(network.network_address),
        "broadcast_address": str(network.broadcast_address),
        "usable_ip_range": f"{network[1]} - {network[-2]}",
        "total_ips": network.num_addresses,
        "usable_ips": network.num_addresses - 2
    }

class SubnetCalculatorView(APIView):
    def get(self, request, ip, mask):
        try:
            result = subnet_calculations(ip, mask)
            return Response(result, status=status.HTTP_200_OK)
        except ValueError:
            return Response({"error": "Invalid IP or mask"}, status=status.HTTP_400_BAD_REQUEST)