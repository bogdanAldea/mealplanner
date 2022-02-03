from django.shortcuts import render, redirect


def AddQuantifiedIngredientToRecipe(request):
    return render(request, "cookbook/forms/add_quantified_ingredients_to_recipe.html")