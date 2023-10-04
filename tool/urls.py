from django.urls import path
from . import views

urlpatterns = [
    path('ip/allocate',views.ip_allocation,name="allocate"),
    path('ip/release/{ipAddress}',views.release_ip,name="release"),
    path('ip/allocated',views.allocated_ips,name="allocated"),
    path('ip/available',views.available_ips,name="available"),
]
