from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cookbook.models import Recipe


@login_required(login_url="users:login")
def RecipeDetailView(request, pk: int):
    """Function based view that allows the user to inspect all the details
    that the Recipe model provides. Each recipe created by the current logged user
    will have its own page where all the details will be displayed."""

    recipe: Recipe = Recipe.objects.get(id=pk)
    context: dict = {"recipe": recipe}

    return render(request, "cookbook/pages/recipe_detail.html", context)