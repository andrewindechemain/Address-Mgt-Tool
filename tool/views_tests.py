from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Address,Customer
import pytest
from django.urls import reverse
import ipaddress


@pytest.mark.django_db
class IPAllocationViewTest(TestCase):
    def setUp(self):
        # Create some IP addresses and customers
        self.ip1 = Address.objects.create(ip="192.168.1.10")
        self.ip2 = Address.objects.create(ip="192.168.1.11", customer="Alice", allocated=True)
        self.user = User.objects.create_user(username="testuser", password="testpass")

    @pytest.mark.django_db
    @pytest.fixture
    def test_ip_allocation_post_success(self):
        # Test the IP allocation view with a valid POST request
        self.client.login(username="testuser", password="testpass")
        data = {"name": "Bob", "email": "bob@example.com"}
        response = self.client.post(reverse("ip_allocation", args=[self.ip1.ip]), data=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {"ip": self.ip1.ip, "customer": "Bob", "email": "bob@example.com"})
        self.ip1.refresh_from_db()
        self.assertEqual(self.ip1.customer, "Bob")
        self.assertEqual(self.ip1.allocated, True)
    
    @pytest.mark.django_db
    @pytest.fixture
    def test_ip_allocation_post_failure(self):
        # Test the IP allocation view with an invalid POST request
        self.client.login(username="testuser", password="testpass")
        data = {"name": "", "email": ""}
        response = self.client.post(reverse("ip_allocation", args=[self.ip1.ip]), data=data)
        self.assertEqual(response.status_code, 400)
        self.ip1.refresh_from_db()
        self.assertIsNone(self.ip1.customer)
        self.assertEqual(self.ip1.allocated, False)
    
    @pytest.mark.django_db
    @pytest.fixture
    def test_ip_allocation_post_no_ip(self):
        # Test the IP allocation view with a non-existing IP address
        self.client.login(username="testuser", password="testpass")
        data = {"name": "Bob", "email": "bob@example.com"}
        response = self.client.post(reverse("ip_allocation", args=["192.168.1.12"]), data=data)
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.content.decode(), "No IPs are available")
    
    @pytest.mark.django_db
    @pytest.fixture
    def test_ip_allocation_get_not_allowed(self):
        # Test the IP allocation view with a GET request
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(reverse("ip_allocation", args=[self.ip1.ip]))
        self.assertEqual(response.status_code, 405)

@pytest.mark.django_db
class ReleaseIPViewTest(TestCase):
    def setUp(self):
        # Create some IP addresses and customers
        self.ip1 = Address.objects.create(ip="192.168.1.10")
        self.ip2 = Address.objects.create(ip="192.168.1.11", customer="Alice", allocated=True)
        self.user = User.objects.create_user(username="testuser", password="testpass")
    
    @pytest.mark.django_db
    @pytest.fixture
    def test_release_ip_put_success(self):
         # Test the release IP view with a valid PUT request
         self.client.login(username="testuser", password="testpass")
         response = self.client.put(reverse("release_ip", args=[self.ip2.ip]))
         self.assertEqual(response.status_code, 200)
         self.assertEqual(response.content.decode(), "successful release ")
         self.ip2.refresh_from_db()
         self.assertIsNone(self.ip2.customer)
         self.assertEqual(self.ip2.allocated, False)
    
    @pytest.mark.django_db
    @pytest.fixture
    def test_release_ip_put_failure(self):
         # Test the release IP view with an invalid PUT request
         self.client.login(username="testuser", password="testpass")
         response = self.client.put(reverse("release_ip", args=[self.ip1.ip]))
         self.assertEqual(response.status_code, 404)
         self.assertEqual(response.content.decode(), "no IP has been allocated")
         self.ip1.refresh_from_db()
         self.assertIsNone(self.ip1.customer)
         self.assertEqual(self.ip1.allocated, False)
    
    @pytest.mark.django_db
    @pytest.fixture
    def test_release_ip_put_no_ip(self):
         # Test the release IP view with a non-existing IP address
         self.client.login(username="testuser", password="testpass")
         response = self.client.put(reverse("release_ip", args=["192.168.1.12"]))
         self.assertEqual(response.status_code, 404)
         self.assertEqual(response.content.decode(), "No IP has been found")
    
    @pytest.mark.django_db
    @pytest.fixture
    def test_release_ip_get_not_allowed(self):
         # Test the release IP view with a GET request
         self.client.login(username="testuser", password="testpass")
         response = self.client.get(reverse("release_ip", args=[self.ip2.ip]))
         self.assertEqual(response.status_code, 405)

@pytest.mark.django_db
class AllocatedIPsViewTest(TestCase):
    def setUp(self):
        # Create some IP addresses and customers
        Address.objects.create(ip="192.168.1.10")
        Address.objects.create(ip="192.168.1.11", customer="Alice", allocated=True)
        Address.objects.create(ip="192.168.1.12", customer="Bob", allocated=True)
        self.user = User.objects.create_user(username="testuser", password="testpass")
    
    @pytest.mark.django_db
    @pytest.fixture
    def test_allocated_ips_get_success(self):
        # Test the allocated IPs view with a valid GET request
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(reverse("allocated_ips"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [
            {"ip": "192.168.1.11", "customer__name": "Alice"},
            {"ip": "192.168.1.12", "customer__name": "Bob"}
        ])
    @pytest.mark.django_db
    @pytest.fixture
    def test_allocated_ips_post_not_allowed(self):
        # Test the allocated IPs view with a POST request
        self.client.login(username="testuser", password="testpass")
        response = self.client.post(reverse("allocated_ips"))
        self.assertEqual(response.status_code, 405)

@pytest.mark.django_db
class AvailableIPsViewTest(TestCase):
    def setUp(self):
        # Create some IP addresses and customers
        Address.objects.create(ip="192.168.1.10")
        Address.objects.create(ip="192.168.1.11", customer="Alice", allocated=True)
        Address.objects.create(ip="192.168.1.12")
        self.user = User.objects.create_user(username="testuser", password="testpass")
    @pytest.mark.django_db
    @pytest.fixture
    def test_available_ips_get_success(self):
         # Test the available IPs view with a valid GET request
         self.client.login(username="testuser", password="testpass")
         response = self.client.get(reverse("available_ips"))
         self.assertEqual(response.status_code, 200)
         self.assertEqual(response.json(), ["192.168.1.10", "192.168.1.12"])

    @pytest.mark.django_db
    @pytest.fixture
    def test_available_ips_post_not_allowed(self):
         # Test the available IPs view with a POST request
         self.client.login(username="testuser", password="testpass")
         response = self.client.post(reverse("available_ips"))
         self.assertEqual(response.status_code, 405)
