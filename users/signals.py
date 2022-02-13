from typing import Any

from django.db.models.signals import post_save
from .models import Cook
import cookbook.models as cb_models
import ingredient.models as ing_models
import pantry.models as pt_models


def add_default_ingredients_to_market(sender, instance, created, **kwargs):

    if created:

        market: ing_models.Market = ing_models.Market.objects.get(cook=instance)
        pantry: pt_models.Pantry = pt_models.Pantry.objects.get(cook=instance)

        ingredient_data: list[dict[str, Any]] = [

            ing_models.Ingredient(name="Carrot", category=ing_models.IngredientCategory.VEGETABLE, market=market),
            ing_models.Ingredient(name="Celery", category=ing_models.IngredientCategory.VEGETABLE, market=market),

            ing_models.Ingredient(name="Bacon", category=ing_models.IngredientCategory.MEAT, market=market),
            ing_models.Ingredient(name="Ground Beef", category=ing_models.IngredientCategory.MEAT, market=market),

            ing_models.Ingredient(name="Banana", category=ing_models.IngredientCategory.FRUIT, market=market),
            ing_models.Ingredient(name="Orange", category=ing_models.IngredientCategory.FRUIT, market=market),

            ing_models.Ingredient(name="Pasta", category=ing_models.IngredientCategory.FLOUR, market=market),
            ing_models.Ingredient(name="Noodles", category=ing_models.IngredientCategory.FLOUR, market=market),

            ing_models.Ingredient(name="Parmesan", category=ing_models.IngredientCategory.DAIRY, market=market),
            ing_models.Ingredient(name="Pecorino", category=ing_models.IngredientCategory.DAIRY, market=market),

            ing_models.Ingredient(name="Soy", category=ing_models.IngredientCategory.SEASONING, market=market),
            ing_models.Ingredient(name="Basil", category=ing_models.IngredientCategory.SEASONING, market=market),

            ing_models.Ingredient(name="Eggs", category=ing_models.IngredientCategory.OTHER, market=market),
            ing_models.Ingredient(name="Rice noodles", category=ing_models.IngredientCategory.OTHER, market=market),
        ]
        ing_models.Ingredient.objects.bulk_create(ingredient_data)


def add_cookbook_to_registered_user(sender, instance, created, **kwargs):

    if created:
        cb_models.CookBook.objects.create(cook=instance)


def add_market_to_registered_user(sender, instance, created, **kwargs):

    if created:
        ing_models.Market.objects.create(cook=instance)


def add_pantry_to_registered_user(sender, instance, created, **kwargs):

    if created:
        pt_models.Pantry.objects.create(cook=instance)


post_save.connect(add_cookbook_to_registered_user, sender=Cook)
post_save.connect(add_market_to_registered_user, sender=Cook)
post_save.connect(add_pantry_to_registered_user, sender=Cook)
post_save.connect(add_default_ingredients_to_market, sender=Cook)