from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from users import forms


def RegisterUserView(request):
    """User registration view that executes a registration form completed and
    submit by a user in order to create a new account. """

    registration_form: forms.UserCreationForm = forms.CreateCookUserForm()
    if request.method == "POST":
        registration_form = forms.CreateCookUserForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            return redirect("users:login")  # redirect user to login page

    context: dict = {"registration_form": registration_form}
    return render(request, "users/pages/register.html", context)
