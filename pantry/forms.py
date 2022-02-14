from django.forms import ModelForm
from .models import InventoryIngredient


class BaseInventoryIngredientForm(ModelForm):
    """Base model form that executes operations on the InventoryIngredient
    model. This form class will be inherited by other classes which will
    implement, if necessary, their own functionality."""

    class Meta:
        model = InventoryIngredient
        fields = ("quantity", )


class UpdateInventoryIngredientForm(BaseInventoryIngredientForm):
    """Model form that handles the update of a given InventoryIngredient object,
    updating its quantity fields."""