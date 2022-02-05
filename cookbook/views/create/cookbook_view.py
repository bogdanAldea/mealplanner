from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cookbook.models import Recipe, CookBook


@login_required(login_url="users:login")
def CookbookView(request):
    cookbook = CookBook.objects.get(cook_user=request.user)
    recipes = Recipe.objects.filter(cookbook=cookbook)

    # split recipe queryset in sub lists of 4 objects each
    split_in_cols: list[list[Recipe]] = [recipes[index: index + 4] for index in range(0, len(recipes), 4)]

    context = {"recipes": recipes, "split_in_cols": split_in_cols}
    return render(request, "cookbook/pages/cookbook.html", context)