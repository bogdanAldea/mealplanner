from django.shortcuts import render, redirect
from ingredient import forms, models


def AddNewIngredientView(request):
    """Function based view that handles the creation a new ingredient model
    using the CreateIngredientForm form."""

    market: models.Market = models.Market.objects.get(cook=request.user)

    create_ingredient_form: forms.CreateIngredientForm = forms.CreateIngredientForm()
    if request.method == "POST":
        create_ingredient_form = forms.CreateIngredientForm(request.POST)
        if create_ingredient_form.is_valid():
            ingredient: models.Ingredient = create_ingredient_form.save(commit=False)
            ingredient.market = market
            ingredient.save()
            return redirect("ingredient:ingredients")
        print(create_ingredient_form.errors)

    context: dict = {
        "ingredient_form": create_ingredient_form,
    }

    return render(request, "ingredient/pages/add_new_ingredient.html", context)