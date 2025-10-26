from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.AddToWishlistAPIView.as_view(), name='add_to_wishlist'),
    path("list/", views.GetWishlistAPIView.as_view(), name='get_wishlist'),
    path("remove/<int:product_id>/", views.RemoveFromWishlistAPIView.as_view(), name='remove_from_wishlist'),
    path("check/<int:product_id>/", views.CheckWishlistAPIView.as_view(), name='check_wishlist'),
]
