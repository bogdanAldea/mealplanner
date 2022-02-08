from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cookbook.models import Recipe, CookBook


@login_required(login_url="users:login")
def CookbookView(request):
    """Function based view that handles the listing of all recipe objects
    which are hold by the current logged user's cookbook objects. """

    cookbook = CookBook.objects.get(cook=request.user)
    recipes = Recipe.objects.filter(cookbook=cookbook)

    context = {"recipes": recipes}
    return render(request, "cookbook/pages/cookbook.html", context)