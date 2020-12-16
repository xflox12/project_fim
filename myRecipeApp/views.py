from django.shortcuts import render, redirect
from django.db.models import Q
from django.db import IntegrityError
from .models import Recipe, RecipeSteps, Ingredient, Category, RecipeCategory
from .forms import create_recipe_form, create_recipe_form2, create_recipe_form3
from myProfileApp.models import Favourite


def recipe_details_view(request, recipe_id=None):
    """Shows detail information of recipe"""
    """This function is used to view the final versions of the recipes created by the users"""
    recipe = None
    if not recipe_id is None:
        recipe = Recipe.objects.get(RecipeId=recipe_id)
        # recipe = get_object_or_404(RecipeId=recipe_id)  # -> single object will be transferred
    context = {
        "recipe": recipe
    }
    return render(request, "details_view_recipe.html", context)


def add_recipe(request, recipe_id=None):
    """This function is used to create and save the basic information of the recipes.
    For example: title, image, number of people and amount of energy."""
    recipe = None
    if not recipe_id is None:
        recipe = Recipe.objects.get(RecipeId=recipe_id)

    if request.method == "POST":
        form1 = create_recipe_form(request.POST, request.FILES or None, instance=recipe)
        if form1.is_valid():
            newrecipe = form1.save(commit=False)
            newrecipe.UserId = request.user
            newrecipe.save()
            recipe = newrecipe
    else:
        form1 = create_recipe_form(request.POST or None, request.FILES or None, instance=recipe)

    context = {
        "form1": form1,
        "recipe": recipe
    }
    return render(request, "dev_add_recipe.html", context)


def add_ingredient(request,recipe_id) :
    """This function is used by users to add all the ingredients of the recipes they create"""
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
            response = redirect('/addrecipe/' + str(recipe_id))
            return response
    else:
        form2 = create_recipe_form2()

    context = {
        "form1": form1,
        "form2": form2,
        "recipe": recipe
    }
    return render(request, template, context)


def add_step(request,recipe_id) :
    """This function is used by users to add all the steps to cook the recipes they want to post"""
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
            response = redirect('/addrecipe/' + str(recipe_id))
            return response
    else:
        form3 = create_recipe_form3()

    context = {
        "form3": form3,
        "recipe": recipe
    }
    return render(request, template, context)


def add_recipe_to_favourites(httprequest):
    """view to mark recipe as favourite and display it under the favourites filter"""

    if httprequest.method == "POST":
        recipe = Recipe.objects.get(RecipeId=httprequest.POST["RecipeId"])
        f = Favourite(UserId=httprequest.user, RecipeId=recipe)
        try:
            f.save()
        except IntegrityError as e:
            if 'UNIQUE constraint' in e.args[0]:
                # accept unique constraint error without any message
                # -> user is not notified when recipes was already marked as favourite
                pass

        return redirect("/home")


def created_recipes_user_temp(httprequest, *args, **kwargs):
    # obj = get_object_or_404(Testmodel, id=my_id)  -> single object will be transferred
    recipes = Recipe.objects.filter(UserId=httprequest.user.id)
    categories = Category.objects.all
    context = {
        "suggestions": ['recipe1', 'recipe2', 'recipe3', 'recipe4'],
        "allRecipes": recipes,
        "categories": categories
    }

    return render(httprequest, 'myCreatedRecipes.html', context)

