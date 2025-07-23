from rest_framework import serializers
from .models import Order,OrderItem
from products.serializers import ProductListSerializer

class OrderitemSerializer(serializers.ModelSerializer):
    product = ProductListSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    items = OrderitemSerializer(read_only = True, many = True)

    class Meta:
        model = Order
        fields = "__all__"