from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .import views

router = DefaultRouter()
# router.register("add_to_cart",views.AddToCartAPIView, basename='add_to_cart')

urlpatterns = [
    path("", include(router.urls)),
    path("add/", views.AddToCartAPIView.as_view(), name='add_to_cart'),
]
