from django.shortcuts import render
from .serializers import UserSeralizer,CustomerAddressSeralizer,RegistrationSerializer,UserLoginSerializer
from .models import CustomUser,CustomerAddress
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from rest_framework.authtoken.models import Token

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.shortcuts import redirect
# Create your views here.
from django.contrib.auth import get_user_model

User = get_user_model()



class UserViewset(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSeralizer


class UserRegistrationApiViewset(APIView):
    serializer_class = RegistrationSerializer
    
    def post(self,request):
        serializer =  self.serializer_class(data=request.data)

        if serializer.is_valid():
            user= serializer.save()
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))

            confirm_link = f"https://shopdrf-production.up.railway.app/users/account/active/{uid}/{token}"

            email_subject = "confirm Your Email"
            email_body = render_to_string('confirm_account_email.html',{'confirm_link':confirm_link})

            email = EmailMultiAlternatives(email_subject,"",to=[user.email])
            email.attach_alternative(email_body,"text/html")
            email.send()
            return Response("Check Your Mail for Confirmation")
        return Response(serializer.errors)

def activate(request,uid64,token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    except(User.DoesNotExist):
        user=None
    
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active=True
        user.save()
        return redirect("https://mew-shop-eight.vercel.app/login")
    return redirect("https://mew-shop-eight.vercel.app/register")


class UserLoginApiView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=self.request.data)

        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username, password=password)

            if user:
                token, _ = Token.objects.get_or_create(user=user)
                login(request, user)
                
                # Return comprehensive user data
                return Response({
                    'token': token.key,
                    'user': {
                        'id': user.id,
                        'username': user.username,
                        'email': user.email,
                        'first_name': user.first_name,
                        'last_name': user.last_name,
                        'is_active': user.is_active,
                        'is_staff': user.is_staff,
                    }
                }, status=200)
            
            return Response({'error': "Invalid Credentials"}, status=401)
        
        return Response(serializer.errors, status=400)
    

class UserLogoutApiView(APIView):
    def get(self,request):
        request.user.auth_token.delete()
        logout(request)

        return Response({"success":"Logout Successfull"})

class CustomerAdressViewset(viewsets.ModelViewSet):
    queryset = CustomerAddress.objects.all()
    serializer_class = CustomerAddressSeralizer