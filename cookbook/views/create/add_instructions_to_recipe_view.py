from django.shortcuts import render, redirect


def AddInstructionToRecipeView(request):
    recipe = request.session.get("new_recipe_instance_id")
    context = {"recipe": recipe}
    return render(request, "cookbook/forms/add_instruction_to_recipe.html", context)