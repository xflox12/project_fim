from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView   #import for class-based-view #import for template-view
# from django.views.generic import TemplateView #add all in one line

# Create your views here.

def home_view(*args, **kwargs):
    return HttpResponse("<h1>Hello World! Hello Flo</h1>")

def home_view_temp(httprequest, *args, **kwargs):             #view with template
    my_dict = {
        "name": "Flo",
        "lastname" : "Schietinger",
        "myList" : ['this', 'is', 'my', 'list']

    }
    return render(httprequest, "home.html", my_dict)


class HomeViewC(View):
    def get(self, *args):
        return HttpResponse("Hello World  from the Class!")
