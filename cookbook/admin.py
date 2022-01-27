from django.contrib import admin
from .models import CookBook, Recipe, QuantifiedIngredient, Instruction


admin.site.register(CookBook)
admin.site.register(Recipe)
admin.site.register(QuantifiedIngredient)
admin.site.register(Instruction)