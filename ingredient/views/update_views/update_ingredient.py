from django.shortcuts import redirect, render
from ingredient import forms, models


def UpdateIngredientView(request, pk: int):
    """Function based view that handles the update of an
    ingredient object filtered by its primary key."""

    ingredient: models.Ingredient = models.Ingredient.objects.get(id=pk)

    update_ingredient_form: forms.UpdateIngredientForm = forms.UpdateIngredientForm(instance=ingredient)
    if request.method == "POST":
        update_ingredient_form = forms.UpdateIngredientForm(request.POST, instance=ingredient)
        if update_ingredient_form.is_valid():
            update_ingredient_form.save()
            return redirect("ingredient:ingredients")

    context: dict = {"ingredient_form": update_ingredient_form}
    return render(request, "ingredient/pages/update_ingredient.html", context)