from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):

    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to="users/user_img/", blank=True, null=True)
    # mobile_no = models.CharField(max_length=12, blank=True, null=True)

    def __str__(self):
        return self.username


class CustomerAddress(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    street = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.customer.email} - {self.street} - {self.city}"
