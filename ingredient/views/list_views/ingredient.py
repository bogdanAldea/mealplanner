from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ingredient.models import Ingredient, Market
from users.models import Cook


@login_required(login_url="users:login")
def IngredientView(request):
    market: Market = Market.objects.get(cook=request.user)
    ingredients: list[Ingredient] = Ingredient.objects.all().filter(market=market)
    context = {"ingredients": ingredients}
    return render(request, "ingredient/pages/ingredients.html", context)