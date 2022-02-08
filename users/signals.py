from django.db.models.signals import post_save
from .models import Cook
import cookbook.models as cb_models
import ingredient.models as ing_models
import pantry.models as pt_models


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