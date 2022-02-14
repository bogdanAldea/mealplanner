from django.urls import path
from .views.list_views import pantry
from .views.update_views import update_inventory_ingredient

app_name = 'pantry'

urlpatterns: list = [
    path("", pantry.PantryView, name="pantry"),
    path("update/<int:pk>/", update_inventory_ingredient.UpdateInventoryIngredientView, name="update")
]