from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from pantry.models import Pantry


@login_required(login_url="users:login")
def PantryView(request):
    pantry: Pantry = Pantry.objects.get(cook=request.user)
    context: dict = {"pantry": pantry}
    return render(request, "pantry/pages/pantry.html", context)