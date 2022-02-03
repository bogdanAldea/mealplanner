from django.forms import ModelForm
from .models import Recipe


class CreateRecipeForm(ModelForm):
    """Model form that handles the creation of a new recipe object.
    After creation the object will be added automatically to user's cookbook."""

    class Meta:
        model = Recipe
        fields = (
            "name", "category", "cooking_time"
        )