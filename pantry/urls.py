from django.urls import path
from .views.menu import pantry_view

app_name = 'pantry'

urlpatterns: list = [
    path("", pantry_view.PantryView, name="pantry"),
]