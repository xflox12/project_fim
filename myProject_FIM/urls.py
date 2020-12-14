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
from django.contrib.auth import views  # Login/Registration
from django.conf import settings
from django.conf.urls.static import static

# Import of the view functions/classes from the view.py file
from myLoginApp.views import user_registration, edit_user_profile
from myNewsletterApp.views import newsletter_signup, newsletter_unsubscribe
from myProfileApp.views import profile_view_temp, profile_change_password
from myRecipeApp.views import list_recipe,  add_recipe, add_ingredient, add_step, \
    add_recipe_to_favourites, recipe_details_view, created_recipes_user_temp
"""list_category,"""
from myStartpageApp.views import home_view_temp, test_view_temp, condition_view_temp, imprint_view_temp, \
    dataprotection_view_temp, faq_view_temp
from myUnitApp.views import list_unit, show_unit, delete_unit, create_unit

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', test_view_temp),  # old
    path('home/', home_view_temp),
    path('terms/', condition_view_temp),
    path('imprint/', imprint_view_temp),
    path('dataprotection/', dataprotection_view_temp),
    path('faq/', faq_view_temp),

    path('reg/', user_registration, name="register"),
    path('', include("django.contrib.auth.urls")),

    path('profile/', profile_view_temp),
    path('change_password/', profile_change_password),
    path('edit_profile/', edit_user_profile),

    path('unit/', list_unit),
    path('unit/create', create_unit),
    path('unit/<str:pk>/', show_unit),
    path('unit/<str:pk>/delete', delete_unit),

    path('signup_newsletter/', newsletter_signup, name='newsletter_signup'),
    path('unsubscribe_newsletter/', newsletter_unsubscribe, name='newsletter_unsubscribe'),

    #path('recipes/', include('myRecipeApp.urls')),
    path('recipe/', list_recipe),
    path('myrecipes/', created_recipes_user_temp),
    path('add_recipe_to_favourites/', add_recipe_to_favourites),
    #path('category/', list_category),
    path('addrecipe/', add_recipe, name='add-recipe'),
    path('viewrecipe/<int:recipe_id>', recipe_details_view, name='view-recipe'),
    path('addrecipe/<int:recipe_id>', add_recipe, name='add-recipe'),
    path('addrecipe/addingredient/<int:recipe_id>', add_ingredient, name='add-ingredient'),
    path('addrecipe/addstep/<int:recipe_id>', add_step, name='add-step'),



    # path('login/', views.LoginView.as_view(), name="login")
    # path('home/<int::my_id>', home_view_temp, name="link-to-home-model"),
    # path('reg/', reg_view_temp),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
