import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Address,Customer
from django.contrib.auth.models import User as AuthUser
from .serializer import AddressSerializer,CustomerSerializer

class IpAllocationView(APIView):
    serializer_class = CustomerSerializer,AddressSerializer
    queryset = Customer.objects.all()

    @login_required
    def post(self, request,user_id, Address):
        AuthUser = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
        data = json.loads(request.body)
        ip = Address.objects.get('ip','customer', 'allocated')
        user = request.user

        if not data.get("name") or not data.get("email"):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if ip:
            ip.customer = Address.objects.name
            ip.allocated = True
            ip.save()
            return Response({'ip': ip.ip, 'customer': ip.customer.name, 'email'
                             : ip.customer.email}, status=status.HTTP_201_CREATED)
        return Response('No IPs are available', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ReleaseIpView(APIView):
    @login_required
    def put(self,Address):
        ip = Address.objects.get('ip', 'customer', 'allocated')
        user = request.user

        if ip.allocated:
            ip.customer = None
            ip.allocated = False
            ip.save()
            return Response('successful released', list(ip.allocated) , status=status.HTTP_200_OK)
        return Response('no IP has been allocated', status=status.HTTP_404_NOT_FOUND)

class AllocatedIpsView(APIView):
    @login_required
    def get(self, request):
        user = request.user
        ips = Address.objects.filter(allocated=True).values('ip', 'customer', 'allocated')
        if ips:
            return Response(list(ips), status=status.HTTP_200_OK)
        return Response('Invalid request method', status=status.HTTP_405_METHOD_NOT_ALLOWED)

class AvailableIpsView(APIView):
    @login_required
    def get(self, request):
        user = request.user
        ips = Address.objects.filter(allocated=False).values_list('ip', flat=True)

        if ips:
            return Response(list(ips), status=status.HTTP_200_OK)
        return Response('Invalid request method', status=status.HTTP_405_METHOD_NOT_ALLOWED)
