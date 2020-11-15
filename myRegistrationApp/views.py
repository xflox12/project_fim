from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView   #import for class-based-view #import for template-view

# Create your views here.

def reg_view_temp(httprequest, *args, **kwargs):             #view with template

    return render(httprequest, "registration.html", {})