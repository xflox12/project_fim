from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse  #For Function-Based-Views
from django.views.generic import View, TemplateView, ListView   #import for class-based-view #import for template-view

#import Models
from .models import Testmodel
from myRecipeApp.models import Recipe, Category

# Create your views here.
def home_view_temp(httprequest, *args, **kwargs):             # view with template
    # obj = get_object_or_404(Testmodel, id=my_id)  ->einzelnes Object wird übergeben
    recipes = Recipe.objects.all()
    recipeOfDay=Recipe.objects.order_by('?').first()
    categories = Category.objects.all
    context = {
        "suggestions": ['recipe1', 'recipe2', 'recipe3', 'recipe4'],
        "allRecipes": recipes,
        "recipeOfDay": recipeOfDay,
        "categories": categories
    }

    return render(httprequest, 'home.html', context)


def condition_view_temp(httprequest, *args, **kwargs):
    return render(httprequest, 'conditions_agb.html')

def imprint_view_temp(httprequest, *args, **kwargs):
    return render(httprequest, 'imprint_impressum.html')

def dataprotection_view_temp(httprequest, *args, **kwargs):
    return render(httprequest, 'dataprotection.html')

def faq_view_temp(httprequest, *args, **kwargs):
    return render(httprequest, 'faq.html')




def test_view_temp(httprequest, *args, **kwargs):
    my_dict = {
        "recipeOfDay": "TestRecipe",
        "lastname": "Schietinger",
        "suggestions": ['recipe1', 'recipe2', 'recipe3', 'recipe4'],
    }
    return render(httprequest, 'index.html', my_dict)


#alternative Methodes to generate a view -> just for Information
class HomeViewC(View):
    def get(self, *args):
        return HttpResponse("Hello World  from the Class!")
def home_view(request):
    return HttpResponse('<h1>Hello World!</h1>')