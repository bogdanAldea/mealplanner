from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from cookbook.models import Recipe, Instruction


def UpdateRecipeInstructionsView(request, pk: int):
    """Function based view that handles the update of a recipe's
    instruction objects. The recipe is returned by filtering its
    primary key and the form updates the instructions attached to
    said recipe."""

    recipe: Recipe = Recipe.objects.get(id=pk)

    UpdateInstructionsFormset = inlineformset_factory(
        parent_model=Recipe, model=Instruction, fields=("step", ), extra=10
    )

    update_instructions_formset: UpdateInstructionsFormset = UpdateInstructionsFormset(instance=recipe)
    if request.method == "POST":
        update_instructions_formset = UpdateInstructionsFormset(request.POST, instance=recipe)
        if update_instructions_formset.is_valid():
            update_instructions_formset.save()
            return redirect("cookbook:update-ingredients", recipe.id)
        print(update_instructions_formset.errors)

    context = {
        "recipe": recipe,
        "is_formset": True,
        "formset": update_instructions_formset
    }

    return render(request, "cookbook/pages/update_instructions.html", context)