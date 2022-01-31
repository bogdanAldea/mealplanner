from django.urls import path
from .views.menu import cookbook_view

app_name = 'cookbook'

urlpatterns: list = [
    path("", cookbook_view.CookbookView, name="cookbook"),
]