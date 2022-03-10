from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cookbook.models import Recipe, QuantifiedIngredient
from collections import Counter


@login_required(login_url="users:login")
def RecipeDetailView(request, pk: int):
    """Function based view that allows the user to inspect all the details
    that the Recipe model provides. Each recipe created by the current logged user
    will have its own page where all the details will be displayed."""

    recipe: Recipe = Recipe.objects.get(id=pk)
    quantified_ingredients: list[QuantifiedIngredient] = QuantifiedIngredient.objects.filter(recipe=recipe)
    # data: dict[str, int] = {
    #     qi.ingredient.category: quantified_ingredients.count(qi.ingredient.category)
    #     for qi in quantified_ingredients
    # }

    data: dict[str, float] = Counter([qi.ingredient.category for qi in quantified_ingredients])
    for k, v in data.items():
        data[k] = v / len(quantified_ingredients) * 100
    context: dict = {"recipe": recipe, "ingredients": quantified_ingredients, "data": dict(data)}

    return render(request, "cookbook/pages/recipe.html", context)