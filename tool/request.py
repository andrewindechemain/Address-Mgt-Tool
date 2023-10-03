import json
import ipaddress
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse, HttpResponse
from .models import IPAddress

@require_http_methods(["POST"])
@login_required

def ip_allocation(request,ipAddress):
    data = json.loads(request.body)
    ip = IPAddress.objects.get(ip=ipAddress.IPv4Address(ip))

    if not data.get("name") or not data.get("email"):
        return HttpResponse(status=400)
    if ip:
        ip.customer = IPAddress.objects.name
        ip.allocated = True
        ip.save()
        return JsonResponse({'ip': ip.ip, 'customer': ip.customer.name, 'email'
                             : ip.customer.email}, status=201)
    else:
        return HttpResponse('No IPs are available', status=500)

@require_http_methods(["PUT"])
@login_required

def release_ip(ipAddress):
    ip = IPAddress.objects.get(ip=ipAddress.IPv4Address(ip))
    if ipaddress.DoesNotExist:
        return HttpResponse('No IP has been found', status=404)
    if ip.allocated:
        ip.customer = None
        ip.allocated = False
        ip.save()
        return HttpResponse('successful release ', status=200)
    else:
        return HttpResponse('no IP has been allocated', status=404)

@require_http_methods(["GET"])
@login_required

def allocated_ips(IPAddress):
    ips = IPAddress.objects.filter(allocated=True).values('ip', 'customer__name', 'email')
    if ips:
        return JsonResponse(list(ips), safe=False, status=200)
    else:
        return HttpResponse('Invalid request method', status=405)
        
@require_http_methods(["GET"])
@login_required

def available_ips(IPAddress):
    ips = IPAddress.objects.filter(allocated=False).values_list('ip', flat=True)

    if ips:
        return JsonResponse(list(ips), safe=False, status=200)
    return HttpResponse('Invalid request method', status=405)
        