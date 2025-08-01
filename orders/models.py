from django.db import models
from products.models import Product
# Create your models here.


class Order(models.Model):
    CURRENCY_CHOICE = [
        ("Pending", "Pending"),
        ("Paid", "Paid"),
    ]
    stripe_checkout_id = models.CharField(max_length=255,unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)
    customer_email = models.EmailField()
    status = models.CharField(max_length=20,choices=CURRENCY_CHOICE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order: {self.stripe_checkout_id} - {self.status}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name="items")
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"Order: {self.product.name} - {self.order.stripe_checkout_id}"