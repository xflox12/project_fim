from django.shortcuts import render, redirect
from django.db.models import Q
from myRecipeApp.models import Recipe, Category

# Create your views here.
def index_temp(httprequest):
    """Function redirects to /home (landing page) after running server"""
    return redirect("/home")


def home_view_temp(httprequest, *args, **kwargs):             # view with template
    """The home_view_temp is the main function which will be called when you are going to the landing page (/home).
    Before rendering the HTML-Template there will be some SQL-Querys to get the desired data from the database
    as all recipes, the recipe of the day (a random recipe which will be generated new each time page is loading) and the categories.
    Also here is the filtering algorithm for the recipes implemented.
    """
    recipes = Recipe.objects.all
    recipeOfDay = Recipe.objects.order_by('?').first()
    categories = Category.objects.all
    message = ""
    isFavourite = True
    favouritesList = Recipe.objects.filter(favourite__UserId=httprequest.user.id)

    if not favouritesList:
        isFavourite = False

    if "query" in httprequest.GET and \
            "filter" in httprequest.GET:
        recipes = Recipe.objects.filter(favourite__UserId=httprequest.user.id)

    elif "query" in httprequest.GET:
        recipes = Recipe.objects.filter(Q(RecipeName__icontains=httprequest.GET["query"]) |
                                        Q(Energy__icontains=httprequest.GET["query"]) |
                                        Q(NumberPeople__icontains=httprequest.GET["query"]))

    elif "filter" in httprequest.GET:
        if httprequest.GET["filter"] == "favourites":
            recipes = Recipe.objects.filter(favourite__UserId=httprequest.user.id)

            print(recipes)

    if "favourites" in httprequest.GET:
        recipes = Recipe.objects.filter(Q(favourite__UserId=httprequest.user.id))
        if not recipes:
            message = "You have not selected any favourites yet"

    if "category" in httprequest.GET:
        recipes = Recipe.objects.filter(Q(recipecategory__CategoryId=httprequest.GET["category"]))
        if not recipes:
            message = "No recipes available in this category"

    context = {
        "allRecipes": recipes,
        "recipeOfDay": recipeOfDay,
        "categories": categories,
        "User": httprequest.user,
        "Message": message,
        "OnHome": True,
        "favouritesList": favouritesList,
        "isFavourite": isFavourite
    }
    return render(httprequest, "home.html", context)


def condition_view_temp(httprequest, *args, **kwargs):
    return render(httprequest, 'conditions_agb.html')


def imprint_view_temp(httprequest, *args, **kwargs):
    return render(httprequest, 'imprint_impressum.html')


def dataprotection_view_temp(httprequest, *args, **kwargs):
    return render(httprequest, 'dataprotection.html')


def faq_view_temp(httprequest, *args, **kwargs):
    return render(httprequest, 'faq.html')

