from django.forms import ModelForm
from .models import Recipe


class BaseRecipeForm(ModelForm):
    """Base form class that handles the creation of a form that allows
    users to manipulate recipe model objects. This form will be subclassed
    by other child forms."""

    class Meta:
        model = Recipe
        fields = (
            "name", "category", "cooking_time"
        )


class CreateRecipeForm(BaseRecipeForm):
    """Form inherits form the BaseRecipeForm in order to create a new form
    that will be used by views to create a new recipe object."""


class UpdateRecipeForm(BaseRecipeForm):
    """Form inherits from the BaseRecipeForm in order to create a new form
    that will be used by views to update existing recipe objects."""