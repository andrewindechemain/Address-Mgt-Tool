"""This file contains model that will be used for the DB 
."""

import ipaddress
from django.db import models

# Create your models here.
# Class that stores customer details
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.name

class Address(models.Model):
    ip = models.GenericIPAddressField(unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    allocated = models.BooleanField(default=False)
    def __str__(self):
        return self.ip

ips_available = [Address(ipaddress.IPv4Address("192.168.1." + str(i))) 
     for i in range(10, 20)]
ips_allocated = []


def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

#Helper function that checks whether an ip addresses are allocated
def is_ip_allocated(ip):
    return any(ip == ip_object.ip for ip_object in 
               ips_allocated) 
  
#Helper function to get IP address object from a list by address
def get_ip_by_address(ips_available, ip_list):
    try:
        ip_obj = ipaddress.ip_address(ips_available)
    except ValueError:
        return None 
    for ip in ip_list:
        if isinstance(ip, ipaddress.IPv4Address) or isinstance(ip, ipaddress.IPv6Address):
            if ip == ip_obj:
                return ip 
    return None 

#Helper function to filter IPs by range
def filter_by_range(ip_list, first, last):
    first = ipaddress.IPv4Address(first)
    last = ipaddress.IPv4Address(last)
    return [ip_object for ip_object in ip_list if ipaddress.IPv4Address(first) <= ipaddress.ip_address(ip_object.ip) <= ipaddress.IPv4Address(last)]

#Helper function to calculate subnet details from a IP and mask
def subnet_calculations(ip,mask):
     network = ipaddress.IPv4Network(f"{ip}/{mask}", strict=False)
     return {
     "network_address": str(network.network_address),
     "broadcast_address": str(network.broadcast_address),
     "usable_ip_range": f"{network[1]} - {network[-2]}",
     "total_ips": network.num_addresses,
     "usable_ips": network.num_addresses - 2
}
