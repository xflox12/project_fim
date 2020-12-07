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
        if request.method == "POST":
            form1 = create_recipe_form()
            form2 = create_recipe_form2()
            form3 = create_recipe_form3()
            if form1.is_valid() and form2.is_valid() and form3.is_valid():
                form1.save()
                form2.save()
                form3.save()
                return redirect("dev_recipe_list.html")
        else:
            form1 = create_recipe_form
            form2 = create_recipe_form2
            form3 = create_recipe_form3
            context = {
                "form1": form1,
                "form2": form2,
                "form3": form3
            }

            return render(request, "dev_add_recipe.html", context)


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
#        if httprequest.user.is_authenticated():
#            username = httprequest.user.username
            recipes = Recipe.objects.filter(Q(recipecategory__CategoryId=httprequest.GET["category"]))
#                                            Q(recipecategory__UserId=username))

    context = {"recipe": recipes, "categories": categories}
    return render(httprequest, "dev_recipe_list.html", context)


def list_category(httprequest):
    categories = Category.objects.all

#    if "query" in httprequest.GET:
#        if "filter" in httprequest.GET:
#            if httprequest.GET["filter"] == "favourites":

    context = {"categories": categories}
    return render(httprequest, "dev_category_list.html", context)
