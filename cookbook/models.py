from django.db import models
from users.models import Cook
from ingredient.models import AbstractComponent, Ingredient


class RecipeCategory(models.TextChoices):
    """Class defines a TextChoice enum object that holds
    string values which represent categories that recipe
    objects fall under."""

    BREAKFAST: str = "Breakfast"
    LUNCH: str = "Lunch"
    MAIN_COURSE: str = "Main Course"
    SNACK: str = "Snack"
    DINNER: str = "Dinner"
    DESSERT: str = "Dessert"


class CookBook(models.Model):
    """Class defines a cookbook object. From the user's account
    the cookbook can be populated with recipes selected and/or
    created by the user. The cookbook model will be used to create_views
    new meal plans and generate text files with shopping lists."""

    cook: Cook = models.OneToOneField(Cook, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cook.__str__()} Cookbook"

    __repr__ = __str__


class Recipe(models.Model):
    """Class defines the modeling of a recipe object. When created by a certain user,
    the recipe will be placed in the user's cookbook automatically."""

    name: str = models.CharField(max_length=50, unique=True)
    category: str = models.CharField(max_length=20, choices=RecipeCategory.choices)
    cooking_time: int = models.PositiveIntegerField()
    cookbook: CookBook = models.ForeignKey(CookBook, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    __repr__ = __str__

    class Meta:
        ordering = ["name"]


class RecipeReferenceMixin(models.Model):
    """Mixin model class that adds a reference to a recipe object
    for the model that mixes the class."""

    recipe: Recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class QuantifiedIngredient(RecipeReferenceMixin, AbstractComponent):
    """Class implements the AbstractComponent class. It defines an object
    that represents an ingredient-quantity pair. Each recipe object will
    create_views its unique pairs to define what the recipe is made of."""

    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"<{self.ingredient}: 10>"

    __repr__ = __str__


class Instruction(RecipeReferenceMixin, models.Model):
    """Class defines a model that will allow users to add
    as many cooking instructions as they want to a recipe object.
    Class uses the RecipeReferenceMixin class to add a reference
    to the recipe the user wants to add the instructions to."""

    step: str = models.TextField(max_length=200)

    def __str__(self):
        return f"{self.recipe.name} instruction"

    __repr__ = __str__