from django.test import TestCase
from django.urls import reverse
from products.models import Category, Product
from reviews.models import Reviews

from users.models import CustomUser

# Create your tests here.

class ReviewsTestCase(TestCase):
    def test_add_review(self):
        user = CustomUser.objects.create(username='AkobirDev', first_name='Akobir')
        user.set_password('somepass')
        user.save()
        
        self.client.login(username='AkobirDev', password='somepass')
        
        c = Category.objects.create(name='catg')
        c.save()
        
        product = Product.objects.create(
            name = 'smth',
            category = c,
            price = 12,
            discount = 0
        )
        
        Reviews.objects.create(
            user = user,
            product = product,
            rating = 3,
            description = 'Nice'
        )
 
        reviews = Reviews.objects.all()

        self.assertEqual(reviews[0].rating, 3)
        self.assertEqual(reviews[0].description, 'Nice')
        self.assertEqual(reviews[0].product, product)
        self.assertEqual(reviews[0].user, user)
