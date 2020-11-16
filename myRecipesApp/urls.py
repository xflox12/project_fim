"""myProject_FIM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#Import of the view functions/classes from the view.py file

from myRecipesApp.views import recipes_list_view_temp, recipes_create_view_temp,recipes_detail_view_temp,recipes_update_view_temp,recipes_delete_view_temp

#remove recipes at the beginning -> already written in the myProject_FIM\urls.py file
# or leave it and the url must be localhost:8080/recipes/recipes/...
urlpatterns = [
    path('recipes/', recipes_list_view_temp, name='recipe-list'),
    path('recipes/create', recipes_create_view_temp, name='recipe-list'),
    #path('recipes/<int::my_id>', recipes_detail_view_temp, name="recipe-detail"),
    #path('recipes/<int::my_id>/update', recipes_update_view_temp, name="recipe-update"),
    #path('recipes/<int::my_id>/delete', recipes_delete_view_temp, name="recipe-delete"),
]
