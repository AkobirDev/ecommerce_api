from django.test import TestCase
from products.models import Category, Product

from users.models import CustomUser

# Create your tests here.
class ProductsTestCase(TestCase):

    def test_add_product(self):
        c = Category.objects.create(name='catg')
        c.save()
        
        Product.objects.create(
            name="smth",
            category=c,
            price=12,
            discount = 0,
        )
        p = Product.objects.get(name='smth')

        self.assertEqual(p.name, 'smth')
        self.assertEqual(p.category, c)
        self.assertEqual(p.price, 12)
        self.assertEqual(p.discount, 0)