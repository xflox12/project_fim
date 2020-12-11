from django.shortcuts import render

# Create your views here.


def profile_view_temp(request, *args, **kwargs):             #view with template
    """ my_dict = {
        "name": "Flo",
        "lastname": "Schietinger",
        "myList": ['this', 'is', 'my', 'list']
    }"""
    user= None
    if user.is_authenticated():
        user=request.user

    return render(request, "myprofile.html", user)
