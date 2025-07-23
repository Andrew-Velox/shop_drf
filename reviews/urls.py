from .import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("all_reviews", views.ReviewViewSet)
router.register("all_ratings", views.ProductRatingViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
