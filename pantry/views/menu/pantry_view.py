from django.shortcuts import render


def PantryView(request):
    return render(request, "pantry/menu/pantry_view.html")