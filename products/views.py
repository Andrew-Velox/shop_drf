from django.shortcuts import render
from rest_framework import viewsets
from .models import Product,Category
from .serializers import ProductListSerializer,CategoryListSerializer,CategoryDetailSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.


class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

    # def get_queryset(self):
    #     queryset = super().get_queryset()

    #     category_id = self

    
    # @action(detail=True, methods=['get'], url_path="details")
    # def product_details(self,request,pk=None):
    #     product = self.get_object()
    #     serializer = ProductListSerializer(product)

    #     return Response(serializer.data)


class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class CategoryDetailsViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer