from django.forms import ModelForm
from .models import Ingredient


class BaseIngredientForm(ModelForm):
    """Model form class that handles the creation of a new
    ingredient object."""

    class Meta:
        model = Ingredient
        fields = "__all__"
        exclude = ("market", )


class CreateIngredientForm(BaseIngredientForm):
    """"""


class UpdateIngredientForm(BaseIngredientForm):
    """"""