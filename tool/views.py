"""Django configurations for the view of the App
   It configures Authorization decorators and responses to requests
."""
import json
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse, HttpResponse
from .models import Address

@require_http_methods(["POST"])
@login_required

def ip_allocation(request,Address):
    data = json.loads(request.body)
    ip = Address.objects.get(ip=Address.IPv4Address(ip))

    if not data.get("name") or not data.get("email"):
        return HttpResponse(status=400)
    if ip:
        ip.customer = Address.objects.name
        ip.allocated = True
        ip.save()
        return JsonResponse({'ip': ip.ip, 'customer': ip.customer.name, 'email'
                             : ip.customer.email}, status=201)
    return HttpResponse('No IPs are available', status=500)

@require_http_methods(["PUT"])
@login_required

def release_ip(Address):
    ip = Address.objects.get(ip=Address.IPv4Address(ip))
    if Address.DoesNotExist:
        return HttpResponse('No IP has been found', status=404)
    if ip.allocated:
        ip.customer = None
        ip.allocated = False
        ip.save()
        return HttpResponse('successful release ', status=200)
    return HttpResponse('no IP has been allocated', status=404)

@require_http_methods(["GET"])
@login_required

def allocated_ips(Address):
    ips = Address.objects.filter(allocated=True).values('ip', 'customer__name', 'email')
    if ips:
        return JsonResponse(list(ips), safe=False, status=200)
    return HttpResponse('Invalid request method', status=405)

@require_http_methods(["GET"])
@login_required

def available_ips(Address):
    ips = Address.objects.filter(allocated=False).values_list('ip', flat=True)

    if ips:
        return JsonResponse(list(ips), safe=False, status=200)
    return HttpResponse('Invalid request method', status=405)
        