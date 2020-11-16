from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse  # For Function-Based-Views
from django.views.generic import View, TemplateView, ListView

#import Models
#from .models import PlaceholderModel

# Create your views here.



# Create your views here.
def recipes_list_view_temp(httprequest, my_id, *args, **kwargs):             #view with template

    return render(httprequest, '../myRecipesApp/templates/recipes.html', {})

def recipes_create_view_temp(httprequest, my_id, *args, **kwargs):             #view with template

    return render(httprequest, '../myRecipesApp/templates/recipes.html', {})

def recipes_detail_view_temp(httprequest, my_id, *args, **kwargs):             #view with template

    return render(httprequest, '../myRecipesApp/templates/recipes.html', {})

def recipes_update_view_temp(httprequest, my_id, *args, **kwargs):             #view with template

    return render(httprequest, '../myRecipesApp/templates/recipes.html', {})

def recipes_delete_view_temp(httprequest, my_id, *args, **kwargs):             #view with template

    return render(httprequest, '../myRecipesApp/templates/recipes.html', {})




