from django.contrib import admin
from .models import Booking, Customer, Car, Rating, Comment, Category


# Register your models here.
admin.site.register(Booking)


class BookingInlines(admin.TabularInline):
    model = Booking
    fieldsets = [(None, {"fields": ["car", "processed", "date"]})]
    readonly_fields = ("date",)
    extra = 0


class RatingInlines(admin.TabularInline):
    model = Rating
    fieldsets = [(None, {"fields": ["rate"]})]
    extra = 0


class CommentInlines(admin.TabularInline):
    model = Comment
    fieldsets = [(None, {"fields": ["comment"]})]
    extra = 0


class CarInlines(admin.TabularInline):
    model = Car
    fieldsets = [(None, {"fields": ["model", "quantity"]})]
    extra = 0


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    inlines = [
        BookingInlines,
    ]


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    inlines = [
        BookingInlines,
        RatingInlines,
        CommentInlines,
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        CarInlines,
    ]
