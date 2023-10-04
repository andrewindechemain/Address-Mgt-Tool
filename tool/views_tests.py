# test.py
from django.test import TestCase, Client
import pytest
from django.contrib.auth.models import User
from .models import Address, Customer

@pytest.mark.django_db
class ViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.customer = Customer.objects.create(name='testcustomer', email='test@test.com')
        self.ip1 = Address.objects.create(ip='192.168.0.1', allocated=False)
        self.ip2 = Address.objects.create(ip='192.168.0.2', allocated=True, customer=self.customer)

    @pytest.mark.django_db
    def test_ip_allocation(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post('/ip_allocation/192.168.0.1/', {'name': 'newcustomer', 'email': 'new@test.com'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'ip': '192.168.0.1', 'customer': 'newcustomer', 'email': 'new@test.com'})
        self.assertTrue(Address.objects.get(ip='192.168.0.1').allocated)
        self.assertEqual(Address.objects.get(ip='192.168.0.1').customer.name, 'newcustomer')
    
    @pytest.mark.django_db
    def test_ip_allocation_invalid_data(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post('/ip_allocation/192.168.0.1/', {'name': '', 'email': ''})
        self.assertEqual(response.status_code, 400)
    
    @pytest.mark.django_db
    def test_ip_allocation_no_ip_available(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post('/ip_allocation/192.168.0.3/', {'name': 'newcustomer', 'email': 'new@test.com'})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.content, b'No IPs are available')
    
    @pytest.mark.django_db
    def test_release_ip(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.put('/release_ip/192.168.0.2/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'successful release ')
        self.assertFalse(Address.objects.get(ip='192.168.0.2').allocated)
        self.assertIsNone(Address.objects.get(ip='192.168.0.2').customer)
    
    @pytest.mark.django_db
    def test_release_ip_no_ip_allocated(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.put('/release_ip/192.168.0.1/')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.content, b'no IP has been allocated')
    
    @pytest.mark.django_db
    def test_allocated_ips(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get('/allocated_ips/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [{'ip': '192.168.0.2', 'customer__name': 'testcustomer', 'email': 'test@test.com'}])
    
    @pytest.mark.django_db
    def test_available_ips(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get('/available_ips/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), ['192.168.0.1'])
