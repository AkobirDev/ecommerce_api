from django.contrib import admin

from reviews.models import Reviews

# Register your models here.
@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('description', 'rating', 'product', 'user')