from django.test import TestCase
from django.urls import reverse
from payments.models import Payment
from products.models import Order

from users.views import User

# Create your tests here.

class PaymentTestCase(TestCase):
    def SetUp(self):
        return super().setUp()

    def test_payment(self):
        user = User.objects.create(
            username = 'Akobir',
            email = 'akobir@mail.ru',
        )
        user.set_password('somepass')
        user.save()

        order = Order.objects.create(user=user)
        order.save()
        payment = Payment.objects.create(
            order=order, 
            amount=123.45,
            payment_method = 'CASH', 
            )
        payment.save()

        self.assertEqual(payment.order, order)
        self.assertEqual(payment.amount, 123.45)
        self.assertEqual(payment.payment_method, 'CASH')
