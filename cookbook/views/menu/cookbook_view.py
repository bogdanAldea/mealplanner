from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="users:login")
def CookbookView(request):
    return render(request, "cookbook/menu/cookbook_view.html")