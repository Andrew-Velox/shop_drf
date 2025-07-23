from rest_framework import serializers
from customers.serializers import UserSeralizer
from .models import ProductRating,Review

class ReviewSerializer(serializers.ModelSerializer):
    user = UserSeralizer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'

class ProductRatingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductRating
        fields = "__all__"