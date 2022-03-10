from django.forms import inlineformset_factory
from django.shortcuts import redirect, render
from cookbook.models import Recipe, QuantifiedIngredient


def UpdateQuantifiedIngredientsView(request, pk: int):
    """Function based view that handles the update of a recipe's
    quantified ingredient objects. The recipe is returned by filtering its
    primary key and the form updates the ingredients attached to
    said recipe."""

    recipe: Recipe = Recipe.objects.get(id=pk)

    UpdateQuantifiedIngredientsFormset = inlineformset_factory(
        parent_model=Recipe, model=QuantifiedIngredient, fields=("ingredient", "quantity", ), extra=0
    )

    update_quantified_ingredient_form: UpdateQuantifiedIngredientsFormset = UpdateQuantifiedIngredientsFormset(instance=recipe)
    if request.method == "POST":
        update_quantified_ingredient_form = UpdateQuantifiedIngredientsFormset(request.POST, instance=recipe)
        if update_quantified_ingredient_form.is_valid():
            update_quantified_ingredient_form.save()
            return redirect("cookbook:cookbook")

    context = {
        "formset": update_quantified_ingredient_form,
        "is_formset": True,
        "recipe": recipe
    }

    return render(request, "cookbook/pages/update_quantified_ingredients.html", context)