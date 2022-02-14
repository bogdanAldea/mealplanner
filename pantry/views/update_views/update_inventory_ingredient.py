from django.shortcuts import redirect, render
from pantry import models, forms


def UpdateInventoryIngredientView(request, pk: int):
    """Function based view that handles the update of an ingredient's quantity
    value in the pantry application filtered by its primary key."""

    ingredient: models.InventoryIngredient = models.InventoryIngredient.objects.get(id=pk)

    update_quantity_form: forms.UpdateInventoryIngredientForm = forms.UpdateInventoryIngredientForm(
        instance=ingredient
    )
    if request.method == "POST":
        update_quantity_form = forms.UpdateInventoryIngredientForm(request.POST, instance=ingredient)
        if update_quantity_form.is_valid():
            update_quantity_form.save()
        return redirect("pantry:pantry")

    context: dict = {"update_quantity_form": update_quantity_form, "ingredient": ingredient}
    return render(request, "pantry/pages/update_inventory_ingredient.html", context)