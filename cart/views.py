from django.shortcuts import render
from rest_framework import status
from .models import Cart,CartItem,Product
from .serializers import CartSerializer, CartItemSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

class AddToCartAPIView(APIView):
    """Add a product to cart or increment quantity if already exists"""
    
    def post(self, request):
        cart_code = request.data.get("cart_code")
        product_id = request.data.get("product_id")
        quantity = request.data.get("quantity", 1)

        if not cart_code or not product_id:
            return Response(
                {"error": "cart_code and product_id are required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            cart, _ = Cart.objects.get_or_create(cart_code=cart_code)
            product = Product.objects.get(id=product_id)
            cart_item, created = CartItem.objects.get_or_create(
                cart=cart,
                product=product
            )
            
            if created:
                cart_item.quantity = quantity
            else:
                cart_item.quantity += int(quantity)
            
            cart_item.save()

            serializer = CartSerializer(cart)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Product.DoesNotExist:
            return Response(
                {"error": "Product not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error": str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class GetCartAPIView(APIView):
    """Get cart details with all items"""
    
    def get(self, request, cart_code):
        try:
            cart = Cart.objects.get(cart_code=cart_code)
            serializer = CartSerializer(cart)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Cart.DoesNotExist:
            return Response(
                {"error": "Cart not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )


class UpdateCartItemAPIView(APIView):
    """Update quantity of a cart item"""
    
    def patch(self, request, item_id):
        quantity = request.data.get("quantity")
        
        if quantity is None:
            return Response(
                {"error": "quantity is required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            cart_item = CartItem.objects.get(id=item_id)
            cart_item.quantity = int(quantity)
            
            if cart_item.quantity <= 0:
                cart_item.delete()
                return Response(
                    {"message": "Item removed from cart"},
                    status=status.HTTP_200_OK
                )
            
            cart_item.save()
            serializer = CartItemSerializer(cart_item)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except CartItem.DoesNotExist:
            return Response(
                {"error": "Cart item not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class RemoveFromCartAPIView(APIView):
    """Remove an item from cart"""
    
    def delete(self, request, item_id):
        try:
            cart_item = CartItem.objects.get(id=item_id)
            cart_item.delete()
            return Response(
                {"message": "Item removed from cart"},
                status=status.HTTP_200_OK
            )
        except CartItem.DoesNotExist:
            return Response(
                {"error": "Cart item not found"},
                status=status.HTTP_404_NOT_FOUND
            )


class ClearCartAPIView(APIView):
    """Clear all items from cart"""
    
    def delete(self, request, cart_code):
        try:
            cart = Cart.objects.get(cart_code=cart_code)
            cart.cartitems.all().delete()
            return Response(
                {"message": "Cart cleared successfully"},
                status=status.HTTP_200_OK
            )
        except Cart.DoesNotExist:
            return Response(
                {"error": "Cart not found"},
                status=status.HTTP_404_NOT_FOUND
            )