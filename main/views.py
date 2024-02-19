from django.shortcuts import render, redirect
from main.forms import SeriesForm
from main.models import Item
from django.http import HttpResponse
from django.core import serializers

def show_main(request):
    series = Item.objects.all()

    context = {
        'name': 'Kania Almyra Bilqist',
        'class': 'PBP A',
        'series': series 
    }

    return render(request, "main.html", context)

def create_series(request):
    form = SeriesForm(request.POST or None) 

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_series.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")