from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="users:login")
def PantryView(request):
    return render(request, "pantry/menu/pantry_view.html")