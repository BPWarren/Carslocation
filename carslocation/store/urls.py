from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>/", views.car_details, name="details"),
    path("<str:categoryname>/", views.liste_percategory, name="categorypage"),
]
