from django.contrib import admin

from.models import Recipe
from.models import RecipeSteps
from.models import FoodItem
from.models import Ingredient
from.models import RecipeCategory
from.models import Category
from.models import Rating
from .models import RecipeComment


# Register your models here.
admin.site.register(Recipe)
admin.site.register(RecipeSteps)
admin.site.register(FoodItem)
admin.site.register(Ingredient)
admin.site.register(RecipeCategory)
admin.site.register(Category)
admin.site.register(Rating)
admin.site.register(RecipeComment)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)