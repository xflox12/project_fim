from django.shortcuts import render

# Create your views here.


def profil_view_temp(httprequest, *args, **kwargs):             #view with template
    my_dict = {
        "name": "Flo",
        "lastname" : "Schietinger",
        "myList" : ['this', 'is', 'my', 'list']

    }
    return render(httprequest, "../myProfilApp/templates/myprofil.html", my_dict)
