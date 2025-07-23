from rest_framework import serializers
from .models import Wishlist
from customers.serializers import UserSeralizer
from products.serializers import ProductListSerializer


class WishlistSerializer(serializers.ModelSerializer):
    user = UserSeralizer(read_only=True)
    product = ProductListSerializer(read_only =True)

    class Meta:
        model = Wishlist
        fields = "__all__"
        