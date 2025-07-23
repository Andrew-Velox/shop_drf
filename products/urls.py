from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .import views

router = DefaultRouter()
router.register("list",views.ProductViewset)
router.register("category",views.CategoryViewset)
router.register("details",views.CategoryDetailsViewset, basename="category-details")

urlpatterns = [
    path("", include(router.urls)),
]
