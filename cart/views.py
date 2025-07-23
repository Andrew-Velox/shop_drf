from django.shortcuts import render
from rest_framework import status
from .models import Cart,CartItem,Product
from .serializers import CartSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

class AddToCartAPIView(APIView):
    
    def post(self,request):
        cart_code = request.data.get("cart_code")
        product_id = request.data.get("product_id")

        if not cart_code or not product_id:
            return Response({"error":"cart_code and product_id are required"})
        
        try:
            cart, _ = Cart.objects.get_or_create(cart_code=cart_code)
            product = Product.objects.get(id=product_id)
            cart_item, _ = CartItem.objects.get_or_create(cart=cart,product=product)
            

            cart_item.quantity =1
            cart_item.save()

            serializer = CartSerializer(cart)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Product.DoesNotExist:
            return Response({"error":"Product not found"}, status=status.HTTP_404_NOT_FOUND)