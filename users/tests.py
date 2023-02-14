from django.test import TestCase
from django.urls import reverse

from users.models import CustomUser

# Create your tests here.

class UserTestCase(TestCase):
	def setUp(self):
		CustomUser.objects.create_user(username="AkobirDev", password="my_pass", email="example@gmail.com")
		CustomUser.objects.create_superuser(username="adminn")
        
	def test_user(self):
		user = CustomUser.objects.get(username="AkobirDev")
		self.assertEqual(user.username, "AkobirDev")
		self.assertEqual(user.email, "example@gmail.com")
		self.assertEqual(user.is_staff, False)

	def test_admin_user(self):
		admin = CustomUser.objects.get(username="adminn")
		self.assertEqual(admin.is_staff, True)

