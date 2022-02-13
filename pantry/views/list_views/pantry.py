from django.shortcuts import render
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required
from pantry.models import Pantry, InventoryIngredient


@login_required(login_url="users:login")
def PantryView(request):
    """Function based view that handles the listing of all inventory ingredients
    which are hold by the Pantry objects related to the current logged user."""

    pantry: Pantry = Pantry.objects.get(cook=request.user)

    UpdateInventoryIngredientFormset = inlineformset_factory(
        parent_model=Pantry, model=InventoryIngredient, fields=("quantity", ), extra=0
    )

    formset: UpdateInventoryIngredientFormset = UpdateInventoryIngredientFormset(instance=pantry)
    if request.method == "POST":
        formset = UpdateInventoryIngredientFormset(request.POST, intance=pantry)
        if formset.is_valid():
            formset.save()

    context: dict = {"pantry": pantry, "formset": formset, "is_formset": True}
    return render(request, "pantry/pages/pantry.html", context)