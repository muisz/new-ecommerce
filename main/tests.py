from django.test import TestCase
from django.conf import settings
from main.models.product import Shops

# Create your tests here.
class AddCustomerTesting(TestCase):
    def test_add_customer(self):
        saved = Shops.objects.create(
                customer_id=1,
                name="Testing Shop",
                bio="my testing shop",
                url="/testing-shop"
        )
        self.assertEqual(saved.customer_id, 1)
        self.assertEqual(saved.name, "Testing Shop")
        self.assertEqual(saved.bio, "my testing shop")
        self.assertEqual(saved.url, "/testing-shop")
        saved.delete()
