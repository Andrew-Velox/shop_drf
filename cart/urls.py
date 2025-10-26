from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("add/", views.AddToCartAPIView.as_view(), name='add_to_cart'),
    path("get/<str:cart_code>/", views.GetCartAPIView.as_view(), name='get_cart'),
    path("update/<int:item_id>/", views.UpdateCartItemAPIView.as_view(), name='update_cart_item'),
    path("remove/<int:item_id>/", views.RemoveFromCartAPIView.as_view(), name='remove_from_cart'),
    path("clear/<str:cart_code>/", views.ClearCartAPIView.as_view(), name='clear_cart'),
]
