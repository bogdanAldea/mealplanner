from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="users:login")
def IngredientView(request):
    return render(request, "ingredient/menu/ingredient_view.html")