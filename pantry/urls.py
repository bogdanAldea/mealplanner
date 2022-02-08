from django.urls import path
from .views.list_views import pantry

app_name = 'pantry'

urlpatterns: list = [
    path("", pantry.PantryView, name="pantry"),
]