from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from cookbook.models import Recipe, QuantifiedIngredient


def AddQuantifiedIngredientToRecipeView(request):
    """Function based view that handles the creation of new quantified ingredients
    for new recipe objects. Similar to AddInstructionToRecipeView, the newly created recipe
    objects will be passed to this view in order to ingredient objects to be attached to it."""

    saved_session_obj_id: int = request.session.get("new_recipe_instance_id")
    recipe: Recipe = Recipe.objects.get(id=saved_session_obj_id)
    quantified_ingredients: list[QuantifiedIngredient] = QuantifiedIngredient.objects.filter(recipe=recipe)

    QuantifiedIngredientFormset: type = inlineformset_factory(
        parent_model=Recipe, model=QuantifiedIngredient, fields=("ingredient", "quantity", ), extra=1
    )

    add_quantified_ingredient_formset: QuantifiedIngredientFormset = QuantifiedIngredientFormset()
    if request.method == "POST":
        add_quantified_ingredient_formset = QuantifiedIngredientFormset(request.POST, instance=recipe)
        if add_quantified_ingredient_formset.is_valid():
            add_quantified_ingredient_formset.save()
            return redirect("cookbook:add-ingredients")

    context: dict = {
        "recipe": recipe,
        "is_formset": True,
        "formset": add_quantified_ingredient_formset,
        "ingredients": quantified_ingredients,
    }

    return render(request, "cookbook/pages/add_quantified_ingredients.html", context)