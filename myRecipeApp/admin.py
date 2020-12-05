from django.contrib import admin

from.models import Recipe
from.models import RecipeSteps
from.models import FoodItem
from.models import Ingredient
from.models import RecipeCategory
from.models import Category


# Register your models here.
admin.site.register(Recipe)
admin.site.register(RecipeSteps)
admin.site.register(FoodItem)
admin.site.register(Ingredient)
admin.site.register(RecipeCategory)
admin.site.register(Category)