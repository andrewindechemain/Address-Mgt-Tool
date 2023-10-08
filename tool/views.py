from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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
from drf_yasg.generators import OpenAPISchemaGenerator



class IpAllocationView(APIView):
  serializer_class = IpAllocationSerializer
  def post(self, request, **kwargs):
    customer_id = request.data.get('customer_id')
    email = kwargs.get('email')
    name = kwargs.get('name')
    customer = get_object_or_404(Customer, pk=customer_id, email=email, name=name)    
    ip = Address.objects.filter(allocated=False).first()
    if ip:
      ip.customer = customer
      ip.allocated = True
      ip.save()
      serializer = self.serializer_class(ip)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response("No IP address available", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

class ReleaseIpView(APIView):
    def put(self, request, ipAddress):
        ip = get_object_or_404(Address, ip=ipAddress)
        if ip.allocated:
            ip.customer = None
            ip.allocated = False
            ip.save()
            return Response({'message': 'IP successfully released', 'ip': ip}, status=status.HTTP_200_OK)
        return Response('No IP has been allocated', status=status.HTTP_404_NOT_FOUND)

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
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response('Invalid request method', status=status.HTTP_405_METHOD_NOT_ALLOWED)

class CustomSchemaGenerator(OpenAPISchemaGenerator):
    def get_endpoints(self, request):
        endpoints = super().get_endpoints(request)
        filtered_endpoints = {}
        for path, (method, view) in endpoints.items():
           if view.has_permission(request):
                filtered_endpoints[path] = (method, view)
        return filtered_endpoints