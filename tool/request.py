from django.db import models
from .models import Customer
import json
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

@require_http_methods(["POST"])
@login_required

#Check/Validate customer name and email 
def ip_allocation(request):
    data = json.loads(request.body)

    if not data.get("customer_name") or not data.get("email"):
        return HttpResponse(status=400)
    
    if not ips_available:
        return HttpResponse(status=500)
    