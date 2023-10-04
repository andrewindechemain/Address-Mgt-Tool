"""This file contains test cases for the models that have been created
   Assertions are used to pass or fail the tests 
."""
import pytest
from django.urls import reverse
from .models import Customer, Address, is_ip_valid, is_ip_allocated, get_ip_by_address, filter_by_range, subnet_calculations

# Mark the test functions that need database access
@pytest.mark.django_db
# Create some fixtures for customers and IP addresses
@pytest.fixture
def customers():
    # Create some customers and return them as a list
    andrew = Customer.objects.create(name="Andrew", email="andrew@example.com")
    indeche = Customer.objects.create(name="Indeche", email="indeche@example.com")
    peter = Customer.objects.create(name="Peter", email="peter@example.com")
    return [andrew, indeche, peter]

@pytest.fixture
def ip_addresses(customers):
    # Create some IP addresses and return them as a list
    andrew, indeche, peter = customers
    ip1 = Address.objects.create(ip="192.168.1.10", customer=andrew, allocated=True)
    ip2 = Address.objects.create(ip="192.168.1.11", customer=indeche, allocated=True)
    ip3 = Address.objects.create(ip="192.168.1.12")
    return [ip1, ip2, ip3]

# Write some test functions for the models and helper functions
def test_customer_str(customers):
    # Test the __str__ method of the Customer model
    andrew, indeche, peter = customers
    assert str(andrew) == "Andrew"
    assert str(indeche) == "Indeche"
    assert str(peter) == "Peter"

def test_customer_email_unique(customers):
    # Test the email field of the Customer model is unique
    with pytest.raises(Exception):
        # Try to create a customer with an existing email
        Customer.objects.create(name="David", email="andrew@example.com")

def test_ipaddress_str(ip_addresses):
    # Test the __str__ method of the Address model
    ip1, ip2, ip3 = ip_addresses
    assert str(ip1) == "192.168.1.10"
    assert str(ip2) == "192.168.1.11"
    assert str(ip3) == "192.168.1.12"

def test_ipaddress_ip_unique(ip_addresses):
    # Test the ip field of the IPAddress model is unique
    with pytest.raises(Exception):
        # Try to create an IP address with an existing ip
        Address.objects.create(ip="192.168.1.10")

def test_ipaddress_customer_on_delete(customers, ip_addresses):
    # Test the customer field of the Address model is set to null on delete
    andrew = customers[0]
    ip = ip_addresses[0]
    andrew.delete()
    ip.refresh_from_db()
    assert ip.customer is None

def test_is_ip_valid():
    # Test the is_ip_valid function
    assert is_ip_valid("192.168.1.10") is True
    assert is_ip_valid("192.168.2.20") is True
    assert is_ip_valid("10.0.0.1") is False
    assert is_ip_valid("invalid") is False

def test_is_ip_allocated(ip_addresses):
     # Test the is_ip_allocated function
     ip1, ip2, ip3 = ip_addresses
     assert is_ip_allocated("192.168.1.10") is True
     assert is_ip_allocated("192.168.1.11") is True
     assert is_ip_allocated("192.168.1.12") is False
     assert is_ip_allocated("192.168.2.20") is False

def test_get_ip_by_address(ip_addresses):
     # Test the get_ip_by_address function
     ip1, ip2, ip3 = ip_addresses
     assert get_ip_by_address("192.168.1.10") == ip1
     assert get_ip_by_address("192.168.1.11") == ip2
     assert get_ip_by_address("192.168.1.12") == ip3
     assert get_ip_by_address("192.168.2.20") is None

def test_filter_by_range(ip_addresses):
      # Test the filter_by_range function
      ip1, ip2, ip3 = ip_addresses
      assert filter_by_range(Address.objects.all(), "192.168.1.10", "192.168.1.12") == [ip1, ip2, ip3]
      assert filter_by_range(Address.objects.all(), "192.168.1.11", "192.168.1.11") == [ip2]
      assert filter_by_range(Address.objects.all(), "192.168.2.10", "192.168.2.20") == []

def test_subnet_calculations():
      # Test the subnet_calculations function
      assert subnet_calculations("192.168.1.10", 24) == {
          "network_address": "192.168.1.0",
          "broadcast_address": "192.168.1.255",
          "usable_ip_range": "192.168.1.1 - 192.168.1.254",
          "total_ips": 256,
          "usable_ips": 254
      }
      assert subnet_calculations("192.168.2.20", 28) == {
          "network_address": "192.168.2.16",
          "broadcast_address": "192.168.2.31",
          "usable_ip_range": "192.168.2.17 - 192.168.2.30",
          "total_ips": 16,
          "usable_ips": 14
      }
