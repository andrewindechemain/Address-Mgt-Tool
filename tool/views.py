from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from .models import Address,Customer
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User as AuthUser
from .serializers import AddressSerializer,CustomerSerializer

class IpAllocationView(APIView):
    serializer_class = CustomerSerializer,AddressSerializer

    @login_required
    def post(self, request,customer_id):
    
        customer = get_object_or_404(Customer, pk=customer_id)
    
        ip = Address.objects.filter(allocated=False).first()

        if ip:
                ip.customer = customer
                ip.allocated = True
                ip.save()   
                return Response(f"IP address {ip} allocated to customer {customer}",
                                    status=status.HTTP_201_CREATED)
        return Response("No IP address available", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

class ReleaseIpView(APIView):
    serializer_class = CustomerSerializer,AddressSerializer
    queryset = Address.objects.all()

    @login_required
    def put(self, request): # Add request parameter here
        ip = get_object_or_404(Address, ip=request.query_params.get("ip")) # Use get_object_or_404 and request.query_params instead of get with multiple fields

        if ip.allocated:
            ip.customer = None
            ip.allocated = False
            ip.save()
            return Response('successful released', list(ip.allocated) , status=status.HTTP_200_OK)
        return Response('no IP has been allocated', status=status.HTTP_404_NOT_FOUND)

class AllocatedIpsView(APIView):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    
    @login_required
    def get(self, request): 
        ips = Address.objects.filter(allocated=True, customer=request.user).values('ip', 'customer', 'allocated') # Use request.user here
        if ips:
            return Response(list(ips), status=status.HTTP_200_OK)
        return Response('Invalid request method', status=status.HTTP_405_METHOD_NOT_ALLOWED)

class AvailableIpsView(APIView):
    @login_required
    def get(self, request):
        ips = Address.objects.filter(allocated=False).values_list('ip', flat=True)

        if ips:
            return Response(list(ips), status=status.HTTP_200_OK)
        return Response('Invalid request method', status=status.HTTP_405_METHOD_NOT_ALLOWED)
