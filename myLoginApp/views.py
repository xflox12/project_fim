from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View   #import for class-based-view
from django.views.generic import TemplateView

# Create your views here.

def home_view(*args, **kwargs):
    return HttpResponse("<h1>Hello World! Hello Flo</h1>")

def home_view_temp(httprequest, *args):             #view with template
    my_dict = {
        "name": "Flo",
    }
    return render(httprequest, "home.html", my_dict)


class HomeViewC(View):
    def get(self, *args):
        return HttpResponse("Hello World  from the Class!")
