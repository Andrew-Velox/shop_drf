from rest_framework import serializers
from .models import Product,Category
from reviews.models import ProductRating,Review
from django.contrib.auth import get_user_model
from reviews.serializers import ReviewSerializer


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = ["id","name","slug","image","price"]
        fields = '__all__'




class ProductRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductRating
        fields = '__all__'

class ProductDetailSerializer(serializers.ModelSerializer):
    review = ReviewSerializer(read_only=True, many=True)
    rating = ProductRatingSerializer(read_only=True)
    poor_review = serializers.SerializerMethodField()
    fair_review = serializers.SerializerMethodField()
    good_review = serializers.SerializerMethodField()
    very_good_review = serializers.SerializerMethodField()
    excellent_review = serializers.SerializerMethodField()

    similar_products = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_similar_products(self,product):
        products = Product.objects.filter(category = product.category).exclude(id=product.id)
        serializer = ProductListSerializer(products,many=True)
        return serializer.data



class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CategoryDetailSerializer(serializers.ModelSerializer):
    products = ProductListSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'