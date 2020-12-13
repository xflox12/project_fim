from django.http import HttpResponse  # For Function-Based-Views
from django.views.generic import View, TemplateView, ListView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.db import IntegrityError
# from .forms import UnitForm
from .models import Recipe, RecipeSteps, Ingredient, Category, RecipeCategory
from .forms import create_recipe_form, create_recipe_form2, create_recipe_form3, CommentForm
from django import forms

#import Models
#from .models import PlaceholderModel

from myProfileApp.models import Favourite
from .forms import favourite_form

def view_recipe(request,recipe_id=None):
    recipe = None
    if not recipe_id is None:
        recipe = Recipe.objects.get(RecipeId=recipe_id)

    context = {
        "recipe": recipe
    }

    return render(request, "dev_view_recipe.html", context)

# Create your views here.
def add_recipe(request,recipe_id=None):
    recipe = None
    if not recipe_id is None:
        recipe = Recipe.objects.get(RecipeId=recipe_id)

    if request.method == "POST":
        form1 = create_recipe_form(request.POST, request.FILES or None, instance=recipe)
        if form1.is_valid() :
            newrecipe = form1.save(commit=False)
            newrecipe.UserId = request.user
            newrecipe.save()
            recipe = newrecipe
    else:
        form1 = create_recipe_form(request.POST or None, request.FILES or None, instance=recipe)

    context = {
        "form1": form1,
        "recipe":recipe
    }

    return render(request, "dev_add_recipe.html", context)

def add_ingredient(request,recipe_id) :
    recipe = None
    if not recipe_id is None:
        recipe = Recipe.objects.get(RecipeId=recipe_id)

    form1 = create_recipe_form(None, None, instance=recipe)
    template = "dev_add_recipe_ingredient.html"
    if request.method == "POST":
        form2 = create_recipe_form2(request.POST or None, request.FILES or None)
        if form2.is_valid():
            newingredient = form2.save(commit=False)
            newingredient.RecipeId = recipe
            newingredient.save()
            response = redirect('/addrecipe/'+str(recipe_id))
            return response
    else :
        form2 = create_recipe_form2()

    context = {
        "form1": form1,
        "form2": form2,
        "recipe": recipe
    }

    return render(request, template, context)

def add_step(request,recipe_id) :
    recipe = None
    if not recipe_id is None:
        recipe = Recipe.objects.get(RecipeId=recipe_id)

    template = "dev_add_recipe_step.html"
    if request.method == "POST":
        form3 = create_recipe_form3(request.POST or None, request.FILES or None)
        if form3.is_valid():
            newstep = form3.save(commit=False)
            newstep.RecipeId = recipe
            newstep.save()
            response = redirect('/addrecipe/'+str(recipe_id))
            return response
    else :
        form3 = create_recipe_form3()

    context = {
        "form3": form3,
        "recipe": recipe
    }

    return render(request, template, context)

def add_comments(request, slug):
    template_name = 'dev_add_comments.html'
    post = get_object_or_404(Recipe, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

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
                                        Q(NumberPeople__icontains=httprequest.GET["query"])
                                        )
        recipes = Recipe.objects.filter(favourite__UserId=httprequest.user.id)

    elif "query" in httprequest.GET:
        recipes = Recipe.objects.filter(Q(RecipeName__icontains=httprequest.GET["query"]) |
                                        Q(Energy__icontains=httprequest.GET["query"]) |
                                        Q(NumberPeople__icontains=httprequest.GET["query"]))

    elif "filter" in httprequest.GET:
        if httprequest.GET["filter"] == "favourites":
            recipes = Recipe.objects.filter(favourite__UserId=httprequest.user.id)

            print(recipes)

    if "category" in httprequest.GET:
#        if httprequest.user.is_authenticated():
#            username = httprequest.user.username
            recipes = Recipe.objects.filter(Q(recipecategory__CategoryId=httprequest.GET["category"]))
#                                            Q(recipecategory__UserId=username))
    context = {"recipe": recipes, "categories": categories, "User": httprequest.user}
    return render(httprequest, "dev_recipe_list.html", context)


def list_category(httprequest):
    categories = Category.objects.all

#    if "query" in httprequest.GET:
#        if "filter" in httprequest.GET:
#            if httprequest.GET["filter"] == "favourites":

    context = {"categories": categories}
    return render(httprequest, "dev_category_list.html", context)

def add_recipe_to_favourites(httprequest):
    if httprequest.method == "POST":
        recipe = Recipe.objects.get(RecipeId=httprequest.POST["RecipeId"])
        f = Favourite(UserId=httprequest.user, RecipeId=recipe)
        try:
            f.save()
        except IntegrityError as e:
            if 'UNIQUE constraint' in e.args[0]:
                # accept unique constraint error without any message
                pass

        return redirect("/recipe")
