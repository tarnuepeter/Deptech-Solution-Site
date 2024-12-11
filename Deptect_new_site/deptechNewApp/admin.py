from django.contrib import admin
from .models import Post, Category, Inquery, Booking


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "created_at"]
    search_fields = ["title", "author", "created_at"]


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("name", "contact", "email", "service")
    search_fields = [
        "service",
    ]


@admin.register(Inquery)
class InqueryAdmin(admin.ModelAdmin):
    list_display = ("name", "contact", "email", "message")


# admin.site.register(Post)
# admin.site.register(Category)
# admin.site.register(Inquery)
# admin.site.register(Booking)
