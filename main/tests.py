from django.test import TestCase
from django.conf import settings
import requests

# Create your tests here.
class AddCustomerTesting(TestCase):
    def test_add_customer(self):
        data = {
            "name":"Abdul Muis",
            "email":"muis@gmail.com",
            "password": "testing",
            "phone": "0881111",
            "provinsi": "Jawa Barat",
            "kabupaten": "Bogor",
            "kecamatan": "Cigudeg",
            "kode_pos": "16660"
        }
        url = '{}/api/main/customers/'.format(settings.MAIN_HOST)
        response = requests.post(url, data = data)
        print(response.content)
        self.assertEqual(response.status_code, 200)
        response2 = requests.post(url, data = data)
        print(response.content)
        self.assertEqual(response2.status_code, 400)
