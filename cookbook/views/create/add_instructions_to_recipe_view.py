from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from cookbook.models import Recipe, Instruction


def AddInstructionToRecipeView(request):
    saved_session_obj_id: int = request.session.get("new_recipe_instance_id")
    recipe: Recipe = Recipe.objects.get(id=saved_session_obj_id)

    InstructionFormset = inlineformset_factory(
        parent_model=Recipe, model=Instruction, fields=("step", ), extra=10
    )

    add_instruction_formset: InstructionFormset = InstructionFormset()
    if request.method == "POST":
        add_instruction_formset = InstructionFormset(request.POST, instance=recipe)
        if add_instruction_formset.is_valid():
            add_instruction_formset.save()
            return redirect("cookbook:add-ingredients")

    context = {
        "recipe": recipe,
        "formset": add_instruction_formset
    }
    return render(request, "cookbook/pages/add_instruction.html", context)