from rest_framework import serializers
from .models import Cart,CartItem
from products.serializers import ProductListSerializer

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductListSerializer(read_only=True)
    sub_total = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = "__all__"

    def get_sub_total(self,cartitem):
        total = cartitem.product.price * cartitem.quantity
        return total


class CartSerializer(serializers.ModelSerializer):
    cartitem = CartItemSerializer(read_only=True, many=True)
    cart_total = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = "__all__"

    def get_cart_total(self,cart):
        items = cart.cartitems.all()
        total = sum([item.quantity * item.product.price for item in items])
        return total

class CartStatSerializer(serializers.ModelSerializer):
    total_quantity = serializers.SerializerMethodField

    class Meta:
        model = Cart
        fields = "__all__"

    def get_total_quantity(self,cart):
        items = cart.cartitems.all()
        total = sum([item.quantity for item in items])
        return total

# class SimpleCartSerializer(serializers.ModelSerializer):
#     num_of_items = serializers.SerializerMethodField

#     class Meta:
#         model = Cart
#         fields = "__all__"

#     def get_total_quantity(self,cart):
#         items = cart.cartitems.all()
#         total = sum([item.quantity for item in items])
#         return total

