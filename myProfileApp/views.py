from django.shortcuts import render

# Create your views here.


def profile_view_temp(httprequest, *args, **kwargs):             #view with template
    my_dict = {
        "name": "Flo",
        "lastname" : "Schietinger",
        "myList" : ['this', 'is', 'my', 'list']

    }
    return render(httprequest, "myprofile.html", my_dict)
