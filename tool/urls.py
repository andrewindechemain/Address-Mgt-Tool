"""
URL configuration for address_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('ip/allocate',views.IpAllocationView.as_view(),name="allocate"),
    path('ip/release/<str:Address>/',views.ReleaseIpView.as_view(),name="release"),
    path('ip/allocated',views.AllocatedIpsView.as_view(),name="allocated"),
    path('ip/available',views.AvailableIpsView.as_view(),name="available"),
]
