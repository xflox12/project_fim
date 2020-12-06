from django.http import HttpResponse  # For Function-Based-Views
from django.views.generic import View, TemplateView, ListView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db.models import Q
# from .forms import UnitForm
from .models import Recipe, RecipeSteps, Ingredient, Category, RecipeCategory
from .forms import create_recipe_form, create_recipe_form2, create_recipe_form3

#import Models
#from .models import PlaceholderModel

# Create your views here.
def add_recipe(request):
    """ this form adds new recipes to the platform. It is only possible to add new recipes if the user is registered
    and, therefore, logged into his/her profile"""
    if not request.user.is_authenticated:
        print("To add a recipe, please log in first")
        return redirect ('/home') # if the user is not logged in, it automatically returns him/her to the home page.
    add_new_recipe = create_recipe_form(request.POST or None)
    add_new_recipe_part2 = create_recipe_form2(request.POST or None)
    add_new_recipe_part3 = create_recipe_form3(request.POST or None)
    if add_new_recipe.is_valid() and add_new_recipe_part2.is_valid() and add_new_recipe_part3.is_valid(): # checks if all the forms/boxes are valid (valid inputs have been introduced)
        print("Your recipe has been added!")
        add_new_recipe.save()
    template="dev_add_recipe.html"
    return render(request, template, {"create_recipe_form": add_new_recipe, "create_recipe_form2": add_new_recipe_part2, "create_recipe_form3": add_new_recipe_part3})


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
    recipes = Recipe.objects.all
    categories = Category.objects.all

    if "query" in httprequest.GET and \
       "filter" in httprequest.GET:
        recipes = Recipe.objects.filter(Q(RecipeName__icontains=httprequest.GET["query"]) |
                                        Q(Energy__icontains=httprequest.GET["query"]) |
                                        Q(NumberPeople__icontains=httprequest.GET["query"])|
                                        Q(favourite__FavouriteId__isnotnull=True))

    elif "query" in httprequest.GET:
        recipes = Recipe.objects.filter(Q(RecipeName__icontains=httprequest.GET["query"]) |
                                        Q(Energy__icontains=httprequest.GET["query"]) |
                                        Q(NumberPeople__icontains=httprequest.GET["query"]))

    elif "filter" in httprequest.GET:
        if httprequest.GET["filter"] == "favourites":
            recipes = Recipe.objects.filter(favourite__FavouriteId__isnull=False)

    if "category" in httprequest.GET:
        if httprequest.user.is_authenticated():
            username = httprequest.user.username
            recipes = Recipe.objects.filter(Q(recipecategory__CategoryId=httprequest.GET["category"]) |
                                            Q(recipecategory__UserId=username))

    context = {"recipe": recipes, "categories": categories}
    return render(httprequest, "dev_recipe_list.html", context)


def list_category(httprequest):
    categories = Category.objects.all

#    if "query" in httprequest.GET:
#        if "filter" in httprequest.GET:
#            if httprequest.GET["filter"] == "favourites":

    context = {"categories": categories}
    return render(httprequest, "dev_category_list.html", context)
