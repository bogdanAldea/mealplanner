from django.shortcuts import render


def IngredientView(request):
    return render(request, "ingredient/menu/ingredient_view.html")