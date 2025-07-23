from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import CustomerAddress

User = get_user_model()


class UserSeralizer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ["id", "email", "username", "first_name", "last_name", "image"]


class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ["username","first_name","last_name","email","password","confirm_password"]
    
    def validate_email(self, value):
        value = value.lower()
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with that email already exists.")
        return value
    
    def validate(self, data):
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        
        if password != confirm_password:
            raise serializers.ValidationError({'confirm_password': "Passwords don't match."})
        
        return data
    
    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email'].lower()
        password = self.validated_data['password']

        account = User(username=username, email=email, first_name=first_name, last_name=last_name)
        account.set_password(password)
        account.is_active = False
        account.save()
        return account

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)

class CustomerAddressSeralizer(serializers.ModelSerializer):
    customer = UserSeralizer(read_only=True)
    class Meta:
        model = CustomerAddress
        fields = '__all__'

