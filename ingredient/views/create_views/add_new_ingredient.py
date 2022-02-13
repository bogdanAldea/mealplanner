from django.shortcuts import render, redirect
from django.db import IntegrityError
from ingredient import forms, models
from pantry.models import Pantry, InventoryIngredient


def AddNewIngredientView(request):
    """Function based view that handles the creation a new ingredient model
    using the CreateIngredientForm form."""

    market: models.Market = models.Market.objects.get(cook=request.user)

    create_ingredient_form: forms.CreateIngredientForm = forms.CreateIngredientForm()
    if request.method == "POST":
        create_ingredient_form = forms.CreateIngredientForm(request.POST)
        if create_ingredient_form.is_valid():

            try:
                ingredient: models.Ingredient = create_ingredient_form.save(commit=False)
                ingredient.market = market
                ingredient.save()

                pantry: Pantry = Pantry.objects.get(cook=request.user)
                inventory_ingredient: InventoryIngredient = InventoryIngredient(
                    ingredient=ingredient,
                    quantity=0,
                    pantry=pantry
                )
                inventory_ingredient.save()

                return redirect("ingredient:ingredients")
            except IntegrityError:
                create_ingredient_form.errors["name"] = create_ingredient_form.error_class(
                    [u'This username is registered.']
                )

    context: dict = {
        "ingredient_form": create_ingredient_form,
    }

    return render(request, "ingredient/pages/add_new_ingredient.html", context)