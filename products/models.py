from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    
class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True, null=True)
    image = models.ImageField(upload_to='products')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    def get_price(self):
        if not self.discount:
            return self.price
        return round(self.price * (100 - self.discount) / 100, 2)

    class Meta:
        ordering = ('-created_at',)

class Order(models.Model):
    # product = models.ForeignKey(Product, on_delete = models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    is_ordered = models.BooleanField(default=False)
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} ordered'


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.quantity} {self.product} by {self.order}'

    def get_total_product_price(self):
        return self.product.get_price() * self.quantity
