from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Wishlist
from .serializers import WishlistSerializer
from products.models import Product
# Create your views here.


class AddToWishlistAPIView(APIView):
    """Add a product to wishlist"""
    # Remove strict authentication requirement for now
    # permission_classes = [IsAuthenticated]
    
    def post(self, request):
        product_id = request.data.get("product_id")
        
        if not product_id:
            return Response(
                {"error": "product_id is required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Check if user is authenticated
        if not request.user.is_authenticated:
            return Response(
                {"error": "Authentication required. Please log in to add items to wishlist."},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        try:
            product = Product.objects.get(id=product_id)
            wishlist_item, created = Wishlist.objects.get_or_create(
                user=request.user,
                product=product
            )
            
            if created:
                serializer = WishlistSerializer(wishlist_item)
                return Response(
                    {"message": "Product added to wishlist", "data": serializer.data},
                    status=status.HTTP_201_CREATED
                )
            else:
                return Response(
                    {"message": "Product already in wishlist"},
                    status=status.HTTP_200_OK
                )
        
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


class GetWishlistAPIView(APIView):
    """Get user's wishlist"""
    # Remove strict authentication requirement
    # permission_classes = [IsAuthenticated]
    
    def get(self, request):
        # Check if user is authenticated
        if not request.user.is_authenticated:
            return Response(
                {"error": "Authentication required. Please log in to view your wishlist."},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        wishlists = Wishlist.objects.filter(user=request.user).order_by('-created')
        serializer = WishlistSerializer(wishlists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RemoveFromWishlistAPIView(APIView):
    """Remove a product from wishlist"""
    # Remove strict authentication requirement
    # permission_classes = [IsAuthenticated]
    
    def delete(self, request, product_id):
        # Check if user is authenticated
        if not request.user.is_authenticated:
            return Response(
                {"error": "Authentication required. Please log in to remove items from wishlist."},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        try:
            wishlist_item = Wishlist.objects.get(
                user=request.user,
                product_id=product_id
            )
            wishlist_item.delete()
            return Response(
                {"message": "Product removed from wishlist"},
                status=status.HTTP_200_OK
            )
        except Wishlist.DoesNotExist:
            return Response(
                {"error": "Product not found in wishlist"},
                status=status.HTTP_404_NOT_FOUND
            )


class CheckWishlistAPIView(APIView):
    """Check if a product is in user's wishlist"""
    # Remove strict authentication requirement
    # permission_classes = [IsAuthenticated]
    
    def get(self, request, product_id):
        # Check if user is authenticated
        if not request.user.is_authenticated:
            return Response(
                {"in_wishlist": False},
                status=status.HTTP_200_OK
            )
        
        exists = Wishlist.objects.filter(
            user=request.user,
            product_id=product_id
        ).exists()
        return Response(
            {"in_wishlist": exists},
            status=status.HTTP_200_OK
        )
