from django.urls import path
from .views.menu import ingredient_view

app_name = 'ingredient'

urlpatterns: list = [
    path("", ingredient_view.IngredientView, name="ingredient"),
]