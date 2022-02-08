from django.db import models


class IngredientCategory(models.TextChoices):
    """Class defines a TextChoice enum object that holds
    string values which represent categories that ingredient
    objects fall under."""

    MEAT: str = "Meat"
    VEGETABLE: str = "Vegetable"
    FRUIT: str = "Fruit"
    DAIRY: str = "Dairy"
    FLOUR: str = "Flour"
    SEASONING: str = "Seasoning"
    OTHER: str = "Other"


class Ingredient(models.Model):
    """Class defines the model that represents an ingredient object."""

    name: str = models.CharField(max_length=50, unique=True)
    category: str = models.CharField(max_length=20, choices=IngredientCategory.choices)

    def __str__(self):
        return self.name

    __repr__ = __str__


class AbstractComponent(models.Model):
    """Class defines an abstract model that will allow other models
    to inherit from without having to instantiate or create_views database
    record of this parent class."""

    ingredient: Ingredient
    quantity: int

    class Meta:
        abstract = True