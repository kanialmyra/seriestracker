from django.shortcuts import render, redirect
from main.forms import SeriesForm
from main.models import Item
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import datetime

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
    # Get data berdasarkan ID
    series = Item.objects.get(pk = id)
    # Hapus data
    series.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))