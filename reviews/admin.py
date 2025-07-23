from django.contrib import admin
from .models import Review,ProductRating

# Register your models here.


class ReviewAdmin(admin.ModelAdmin):
    list_display = ["product","rating","review","created","updated"]

class ProductRatingAdmin(admin.ModelAdmin):
    list_display = ["product","average_rating","total_reviews"]

admin.site.register(Review,ReviewAdmin)
admin.site.register(ProductRating,ProductRatingAdmin)