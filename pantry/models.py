from django.db import models
from ingredient.models import AbstractComponent, Ingredient
from users.models import Cook


class Pantry(models.Model):
    """Model defines a pantry object. When a new user account has been created,
    a new pantry object will be also created from the existing ingredient objects
    at that time in the database."""

    cook: Cook = models.OneToOneField(Cook, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cook.__str__()}'s Pantry"

    __repr__ = __str__


class InventoryIngredient(AbstractComponent):
    """Class implements the AbstractComponent class and implement its fields.
    The model defines a pair of an ingredient object and a quantity value with
    the default value to 0."""

    pantry: Pantry = models.ForeignKey(Pantry, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["ingredient", "pantry"], name="unique_ingredient_pantry")
        ]

    def __str__(self):
        return f"<{self.ingredient.name}: {self.quantity}>"

    __repr__ = __str__