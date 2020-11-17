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
from django.urls import path, include

#Import of the view functions/classes from the view.py file

from myLoginApp.views import profil_view_temp
from myLoginApp.views import user_registration
from myRegistrationApp.views import reg_view_temp
from myStartpageApp.views import home_view_temp
from myRegistrationApp.views import reg_view_temp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view_temp),
    path('recipes/', include('myRecipesApp.urls')),
    path('profil/', profil_view_temp),
    path('reg/', user_registration, name="register"),
    #path('home/<int::my_id>', home_view_temp, name="link-to-home-model"),
    #path('reg/', reg_view_temp),

]
