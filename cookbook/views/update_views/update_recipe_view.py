from django.shortcuts import redirect, render
from cookbook.models import Recipe, CookBook
from cookbook import forms


def UpdateRecipeView(request, pk: int):
    """Function based view that handles the update a recipe object
    selected by its primary key. This form is part of a chain form
    that updates all contained children of the recipe model like Instructions
    and QuantifiedIngredients."""

    cookbook = CookBook.objects.get(cook=request.user)
    recipe = Recipe.objects.get(cookbook=cookbook, id=pk)

    form = forms.UpdateRecipeForm(instance=recipe)
    if request.method == "POST":
        form = forms.UpdateRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect("cookbook:update-instructions", recipe.id)

    context = {
        "recipe": recipe,
        "recipe_form": form
    }

    return render(request, "cookbook/pages/update_recipe.html", context)