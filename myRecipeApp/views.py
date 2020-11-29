from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse  # For Function-Based-Views
from django.views.generic import View, TemplateView, ListView

from django.shortcuts import render, redirect
from django.db.models import Q
# from .forms import UnitForm
from .models import Recipe

#import Models
#from .models import PlaceholderModel

# Create your views here.



# Create your views here.
def recipes_list_view_temp(httprequest, my_id, *args, **kwargs):             #view with template

    return render(httprequest, '../myRecipeApp/templates/recipes.html', {})

def recipes_create_view_temp(httprequest, my_id, *args, **kwargs):             #view with template

    return render(httprequest, '../myRecipeApp/templates/recipes.html', {})

def recipes_detail_view_temp(httprequest, my_id, *args, **kwargs):             #view with template

    return render(httprequest, '../myRecipeApp/templates/recipes.html', {})

def recipes_update_view_temp(httprequest, my_id, *args, **kwargs):             #view with template

    return render(httprequest, '../myRecipeApp/templates/recipes.html', {})

def recipes_delete_view_temp(httprequest, my_id, *args, **kwargs):             #view with template

    return render(httprequest, '../myRecipeApp/templates/recipes.html', {})


def list_recipe(httprequest):
    recipe = Recipe.objects.all
    try:
        if httprequest.GET["query"]:
            recipe = Recipe.objects.filter(Q(RecipeName__icontains=httprequest.GET["query"]) |
                                           Q(Energy__icontains=httprequest.GET["query"]) |
                                           Q(NumberPeople__icontains=httprequest.GET["query"]))
            print(httprequest.GET["query"])
    except KeyError:
        pass
    context = {"recipe": recipe}
    return render(httprequest, "dev_recipe_list.html", context)


