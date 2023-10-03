from django.db import models
import ipaddress

# Create your models here.
# Class that stores customer details
class Customer:
     def __init__(self, ip, customer_name=None, email=None):
          self.ip = ip
          self.customer_name = customer_name
          self.email = email
     def to_dict(self):
        return {
            "ip": str(self.ip),
            "customer_name": self.customer_name,
            "email": self.email
        }
# Lists that store available , allocated or reserved IP addresses
        ips_available = [IPAddress(ipaddress.IPv4Address("192.168.1." + str(i))) 
                        for i in range(10, 20)]
        ips_allocated = []

        ips_reserved = []

# Helper function that checks whether an ip addreesses are valid
     def is_ip_valid(ip):
        try:
            ip = ipaddress.IPv4Address(ip)
            return ip in ipaddress.IPv4Network("192.168.1.0/14")
        except ValueError:
            return False

# Helper function that checks whether an ip addresses are allocated      
     def is_ip_allocated(ip):
        return any(ip == ip_object.ip for ip_object in 
                   ips_allocated)
     
#Helper function to check whether ip addresses are reserved
     def is_ip_reserved(ip):
        return any(ip == ip_object.ip for ip_object in 
                   ips_reserved)
     
#Helper function to get IP address object from a list by address
def get_ip_by_address(ip, ip_list):
    for ip_obj in ip_list:
        if ip == ip_obj.ip:
            return ip_obj
    return None

#Helper function to filter IPs by range
def filter_by_range(ip_list, first, last):
    first = ipaddress.IPv4Address(first)
    last = ipaddress.IPv4Address(last)
    return [ip_object for ip_object in ip_list if first <= ip_object.ip <= last]


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