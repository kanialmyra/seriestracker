from django.shortcuts import render, redirect
from main.forms import SeriesForm
from main.models import Item
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, JsonResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import datetime
import json

@login_required(login_url='/login')
def show_main(request):
    series = Item.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
        'class': 'PBP A',
        'series': series,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def create_series(request):
    form = SeriesForm(request.POST or None) 

    if form.is_valid() and request.method == "POST":
        series = form.save(commit=False)
        series.user = request.user
        series.save()
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

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_series(request, id):
    # Get book berdasarkan ID
    book = Item.objects.get(pk = id)

    # Set book sebagai instance dari form
    form = SeriesForm(request.POST or None, instance=book)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_series.html", context)

def delete_series(request, id):
    series = Item.objects.get(pk = id)
    series.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
def add_series_ajax(request):
    if request.method == 'POST':
        # Retrieve value name, amount, description, and user
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        user = request.user

        # Make a new Item object with those values
        new_series = Item(name=name, amount=amount, description=description, user=user)
        new_series.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def create_series_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)

        new_series = Item.objects.create(
            user = request.user,
            name = data["name"],
            page = int(data["amount"]),
            description = data["description"]
        )

        new_series.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)