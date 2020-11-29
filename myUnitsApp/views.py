from django.shortcuts import render, redirect
from django.db.models import Q
from .forms import UnitForm
from .models import Unit

def create_unit_view(httprequest):
    form = UnitForm()
    if httprequest.POST:
        form = UnitForm(httprequest.POST)
        if form.is_valid():
            form.save()
            return redirect("/units")
    context = {"form": form}
    return render(httprequest, "unit_detail.html", context)

def create_units_view(httprequest):
    units = Unit.objects.all
    try:
        if httprequest.GET["query"]:
            units = Unit.objects.filter(Q(Name__icontains=httprequest.GET["query"]) | Q(Abbreviation__icontains=httprequest.GET["query"]))
            print(httprequest.GET["query"])
    except KeyError:
        pass
    context = {"units": units}
    return render(httprequest, "units_list.html", context)

def delete_unit(httprequest, pk):
    unit = Unit.objects.get(UnitId=pk)
    if httprequest.POST:
        unit.delete()
        return redirect("/units")

def detail_unit_view(httprequest, pk):
    unit = Unit.objects.get(UnitId=pk)
    form = UnitForm(instance=unit)
    if httprequest.POST:
        form = UnitForm(httprequest.POST, instance=unit)
        if form.is_valid():
            form.save()
            return redirect("/units")

    context = {
       'form': form,
       'unit': unit
    }

    return render(httprequest, "unit_detail.html", context)
