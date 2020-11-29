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

# Import of the view functions/classes from the view.py file

from myStartpageApp.views import home_view_temp, test_view_temp
from myProfileApp.views import profile_view_temp
from myLoginApp.views import user_registration
from myUnitsApp.views import create_units_view, detail_unit_view, delete_unit, create_unit_view
from myRegistrationApp.views import reg_view_temp
from django.contrib.auth import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', test_view_temp),
    path('home/', home_view_temp),
    path('recipes/', include('myRecipesApp.urls')),
    path('profile/', profile_view_temp),
    path('reg/', user_registration, name="register"),
    path('units/', create_units_view, name="hello"),
    path('units/create', create_unit_view, name="hello"),
    path('unit/<str:pk>/', detail_unit_view, name="hello"),
    path('unit/<str:pk>/delete', delete_unit, name="hello"),
    path('', include("django.contrib.auth.urls")),

    # path('login/', views.LoginView.as_view(), name="login")

    # path('home/<int::my_id>', home_view_temp, name="link-to-home-model"),
    # path('reg/', reg_view_temp),

]
