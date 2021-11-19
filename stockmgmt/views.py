from django.shortcuts import render
from .models import *
from .forms import StockCreateForm
from django.shortcuts import render, redirect

# Create your views here.


def home(request):
    title = 'Welcome: This is the Home Page'
    form = 'Fomrthis'
    context = {
        "title": title,
        "form": form
    }
    return render(request, "home.html", context)


def list_items(request):
    title = 'Welcome: This is the Home Page'
    quertset = Stock.objects.all()
    context = {
        "title": title,
        "queryset": quertset
    }
    return render(request, "list_items.html", context)


def add_items(request):
    form = StockCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/list_items')
    context = {
        "form": form,
        "title": "Add Item",
    }
    return render(request, "add_items.html", context)
