from django.test import TestCase


# Create your tests here.
from django.test import TestCase
from .models import Customer, IPAddress, is_ip_valid, is_ip_allocated, get_ip_by_address, filter_by_range, subnet_calculations

# Create your tests here.
class CustomerModelTest(TestCase):
    def setUp(self):
        # Create some customers
        Customer.objects.create(name="Andrew", email="andrew@example.com")
        Customer.objects.create(name="Indeche", email="indeche@example.com")
        Customer.objects.create(name="John", email="john@example.com")

    def test_customer_str(self):
        # Test the __str__ method of the Customer model
        andrew = Customer.objects.get(email="andrew@example.com")
        indeche = Customer.objects.get(email="indeche@example.com")
        john = Customer.objects.get(email="john@example.com")
        self.assertEqual(str(andrew), "Andrew")
        self.assertEqual(str(indeche), "Indeche")
        self.assertEqual(str(john), "John")

    def test_customer_email_unique(self):
        # Test the email field of the Customer model is unique
        with self.assertRaises(Exception):
            # Try to create a customer with an existing email
            Customer.objects.create(name="David", email="andrew@example.com")

class IPAddressModelTest(TestCase):
    def setUp(self):
        # Create some IP addresses and customers
        andrew = Customer.objects.create(name="Andrew", email="andrew@example.com")
        indeche = Customer.objects.create(name="Indeche", email="indeche@example.com")
        IPAddress.objects.create(ip="192.168.1.10", customer=andrew, allocated=True)
        IPAddress.objects.create(ip="192.168.1.11", customer=indeche, allocated=True)
        IPAddress.objects.create(ip="192.168.1.12")

    def test_ipaddress_str(self):
        # Test the __str__ method of the IPAddress model
        ip1 = IPAddress.objects.get(ip="192.168.1.10")
        ip2 = IPAddress.objects.get(ip="192.168.1.11")
        ip3 = IPAddress.objects.get(ip="192.168.1.12")
        self.assertEqual(str(ip1), "192.168.1.10")
        self.assertEqual(str(ip2), "192.168.1.11")
        self.assertEqual(str(ip3), "192.168.1.12")

    def test_ipaddress_ip_unique(self):
        # Test the ip field of the IPAddress model is unique
        with self.assertRaises(Exception):
            # Try to create an IP address with an existing ip
            IPAddress.objects.create(ip="192.168.1.10")

    def test_ipaddress_customer_on_delete(self):
        # Test the customer field of the IPAddress model is set to null on delete
        andrew = Customer.objects.get(email="andrew@example.com")
        ip = IPAddress.objects.get(customer=andrew)
        andrew.delete()
        ip.refresh_from_db()
        self.assertIsNone(ip.customer)

class HelperFunctionsTest(TestCase):
    def setUp(self):
        # Create some IP addresses and customers
        andrew = Customer.objects.create(name="Andrew", email="andrew@example.com")
        indeche = Customer.objects.create(name="Indeche", email="indeche@example.com")
        IPAddress.objects.create(ip="192.168.1.10", customer=andrew, allocated=True)
        IPAddress.objects.create(ip="192.168.1.11", customer=indeche, allocated=True)
        IPAddress.objects.create(ip="192.168.1.12")

    def test_is_ip_valid(self):
        # Test the is_ip_valid function
        self.assertTrue(is_ip_valid("192.168.1.10"))
        self.assertTrue(is_ip_valid("192.168.2.20"))
        self.assertFalse(is_ip_valid("10.0.0.1"))
        self.assertFalse(is_ip_valid("invalid"))

    def test_is_ip_allocated(self):
        # Test the is_ip_allocated function
        self.assertTrue(is_ip_allocated("192.168.1.10"))
        self.assertTrue(is_ip_allocated("192.168.1.11"))
        self.assertFalse(is_ip_allocated("192.168.1.12"))
        self.assertFalse(is_ip_allocated("192.168.2.20"))

    def test_get_ip_by_address(self):
         # Test the get_ip_by_address function
         ip1 = IPAddress.objects.get(ip="192.168.1.10")
         ip2 = IPAddress.objects.get(ip="192.168.1.11")
         ip3 = IPAddress.objects.get(ip="192.168.1.12")
         self.assertEqual(get_ip_by_address("192.168.
         1.
         10"), ip1)
         self.assertEqual(get_ip_by_address("192.
         168.
         1.
         11"), ip2)
         self.assertEqual(get_ip_by_address("192.
         168.
         1.
         12"), ip3)
         self.assertIsNone(get_ip_by_address("192.
         168.
         2.
         20"))

    def test_filter_by_range(self):
        # Test the filter_by_range function
        ip1 = IPAddress.objects.get(ip="192.168.1.10")
        ip2 = IPAddress.objects.get(ip="192.168.1.11")
        ip3 = IPAddress.objects.get(ip="192.168.1.12")
        self.assertEqual(filter_by_range(IPAddress.objects.all(), "192.168.1.10", "192.168.1.12"), [ip1, ip2, ip3])
        self.assertEqual(filter_by_range(IPAddress.objects.all(), "192.168.1.11", "192.168.1.11"), [ip2])
        self.assertEqual(filter_by_range(IPAddress.objects.all(), "192.168.2.10", "192.168.2.20"), [])

    def test_subnet_calculations(self):
        # Test the subnet_calculations function
        self.assertEqual(subnet_calculations("192.168.1.10", 24), {
            "network_address": "192.168.1.0",
            "broadcast_address": "192.168.1.255",
            "usable_ip_range": "192.168.1.1 - 192.168.1.254",
            "total_ips": 256,
            "usable_ips": 254
        })
        self.assertEqual(subnet_calculations("192.168.
        2.
        20", 28), {
            "network_address": "192.
            168.
            2.
            16",
            "broadcast_address": "192.
            168.
            2.
            31",
            "usable_ip_range": "192.
            168.
            2.
            17 - 192.
            168.
            2.
            30",
            "total_ips": 16,
            "usable_ips": 14
        })
