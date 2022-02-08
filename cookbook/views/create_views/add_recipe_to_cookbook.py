from django.shortcuts import render, redirect
from cookbook import forms, models


def AddRecipeToCookbookView(request):
    """View function handles the creation of a Recipe objects. Before is beign saved
    to the database, the view assigns the object to the current logged user's cookbook.
    Then, the newly created object's id is saved in the session and passed to views that
    create_views instructions and ingredients for the recipe."""

    cookbook: models.CookBook = models.CookBook.objects.get(cook_user=request.user)

    create_recipe_form: forms.CreateRecipeForm = forms.CreateRecipeForm()
    if request.method == "POST":
        create_recipe_form = forms.CreateRecipeForm(request.POST)
        if create_recipe_form.is_valid():
            recipe: models.Recipe = create_recipe_form.save(commit=False)
            recipe.cookbook = cookbook
            recipe.save()
            request.session["new_recipe_instance_id"] = recipe.id
            return redirect("cookbook:add-instructions")
        else:
            print(create_recipe_form.errors)

    context = {"recipe_form": create_recipe_form, "is_formset": False}
    return render(request, "cookbook/pages/add_recipe.html", context)