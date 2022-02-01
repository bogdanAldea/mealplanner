from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from typing import Any


UserModel: Any = get_user_model()


class CreateCookUserForm(UserCreationForm):

    class Meta:
        model = UserModel
        fields = (
            'first_name', 'last_name', 'username',
            'email', 'password1', 'password2'
        )