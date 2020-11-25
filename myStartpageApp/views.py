from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse  #For Function-Based-Views
from django.views.generic import View, TemplateView, ListView   #import for class-based-view #import for template-view

#import Models
from .models import Testmodel

# Create your views here.
def home_view_temp(httprequest, *args, **kwargs):             #view with template
    #obj = get_object_or_404(Testmodel, id=my_id)  ->einzelnes Object wird übergeben
    obj = Testmodel.objects.all()
    my_dict = {
        "recipeOfDay": "TestRecipe",
        "suggestions": ['recipe1', 'recipe2', 'recipe3', 'recipe4'],
        "name": "Flo",
        "lastname": "Schietinger",
        "myList": ['this', 'is', 'my', 'list'],
        "obj": obj,
    }

    #import all Users from the Model User2
    #allUsers = User2.objects.all()
    # obj = User.objects.get(id=my_id)   -->add my_id as parameter to the function
    # obj = get_object_or_404(User, id=my_id)
    #context = {
        #"allUsers": allUsers,
        #"title": "Our User List"
    #}
    return render(httprequest, 'home.html', my_dict)


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