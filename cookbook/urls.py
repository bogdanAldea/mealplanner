from django.urls import path
from .views.create_views import add_recipe_to_cookbook, add_instructions, add_quantified_ingredients
from .views.list_views import cookbook
from .views.update_views import update_recipe_view, update_instructions, update_quantified_ingredients
from .views.detail_view import recipe

app_name = 'cookbook'

urlpatterns: list = [
    path("", cookbook.CookbookView, name="cookbook"),
    path("recipe/<int:pk>/", recipe.RecipeDetailView, name="recipe-detail"),
    path("add-new-recipe/", add_recipe_to_cookbook.AddRecipeToCookbookView, name="add-new-recipe"),
    path("add-instructions/", add_instructions.AddInstructionToRecipeView, name="add-instructions"),
    path("add-ingredients/", add_quantified_ingredients.AddQuantifiedIngredientToRecipeView, name="add-ingredients"),

    path("update-recipe/<int:pk>/", update_recipe_view.UpdateRecipeView, name="update-recipe"),
    path("update-instructions/<int:pk>/", update_instructions.UpdateRecipeInstructionsView, name="update-instructions"),
    path("update-ingredients/<int:pk>/", update_quantified_ingredients.UpdateQuantifiedIngredientsView, name="update-ingredients"),
]