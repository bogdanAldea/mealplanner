from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ingredient.models import Ingredient, Market
from users.models import Cook


@login_required(login_url="users:login")
def IngredientView(request):
    """Function based view that handles the listing of all ingredient objects
    which are hold in the Market model objects related to the current logged user."""

    market: Market = Market.objects.get(cook=request.user)
    ingredients: list[Ingredient] = Ingredient.objects.all().filter(market=market)

    context = {"ingredients": ingredients}
    return render(request, "ingredient/pages/ingredients.html", context)