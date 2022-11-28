from django.contrib import admin
from .models import Ingredient, Recipe, Recipe_Ingredient, Recipe_Class

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(Recipe_Class)
admin.site.register(Recipe)
admin.site.register(Recipe_Ingredient)