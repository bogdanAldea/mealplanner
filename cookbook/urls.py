from django.urls import path
from .views.create import (cookbook_view, add_recipe_to_cookbook,
                           add_instructions_to_recipe_view, add_quantified_ingredient_to_recipe)

app_name = 'cookbook'

urlpatterns: list = [
    path("", cookbook_view.CookbookView, name="cookbook"),
    path("add-new-recipe/", add_recipe_to_cookbook.AddRecipeToCookbookView, name="add-new-recipe"),
    path("add-instructions/", add_instructions_to_recipe_view.AddInstructionToRecipeView, name="add-instructions"),
    path("add-ingredients/", add_quantified_ingredient_to_recipe.AddQuantifiedIngredientToRecipe, name="add-ingredients"),
]