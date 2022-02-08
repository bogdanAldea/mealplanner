from django.urls import path
from .views.list_views import ingredient
from .views.create_views import add_new_ingredient
from .views.update_views import update_ingredient

app_name = 'ingredient'

urlpatterns: list = [
    path("", ingredient.IngredientView, name="ingredients"),
    path("add-new-ingredient/", add_new_ingredient.AddNewIngredientView, name="add-new-ingredient"),
    path("update-ingredient/<int:pk>/", update_ingredient.UpdateIngredientView, name="update-ingredient"),
]