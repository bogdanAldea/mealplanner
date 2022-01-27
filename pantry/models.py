from django.db import models
from ingredient.models import AbstractComponent, Ingredient
from users.models import Cook


class Pantry(models.Model):
    """Model defines a pantry object. When a new user account has been created,
    a new pantry object will be also created from the existing ingredient objects
    at that time in the database."""

    cook_user: Cook = models.OneToOneField(Cook, on_delete=models.CASCADE)


class InventoryIngredient(AbstractComponent):
    """Class implements the AbstractComponent class and implement its fields.
    The model defines a pair of an ingredient object and a quantity value with
    the default value to 0."""

    pantry: Pantry = models.ForeignKey(Pantry, on_delete=models.CASCADE)
    ingredient = models.OneToOneField(Ingredient, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)