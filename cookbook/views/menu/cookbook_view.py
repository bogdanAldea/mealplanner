from django.shortcuts import render


def CookbookView(request):
    return render(request, "cookbook/menu/cookbook_view.html")