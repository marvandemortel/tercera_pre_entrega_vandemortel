from django.shortcuts import render

from .models import *
from .forms import * 

import sqlite3

def index(request):
    return render(request, "index.html", {'current_path' : request.path})

def about(request):
    return render(request, "about.html", {'current_path' : request.path})

def category(request):
    """
        Muestra TODOS los artículos de TODAS las categorías
    """
    pass
    return render(request, "category.html")

def category_beauty(request):
    """
        Muestra TODOS los artículos de la categoría "Beauty"
    """
    pass
    return render(request, "category_beauty.html", {"posts" : []})

def category_inspiration(request):
    """
        Muestra TODOS los artículos de la categoría "Inspiration"
    """
    pass
    return render(request, "category_inspiration.html", {"posts" : []})

def category_lifestyle(request):
    """
        Muestra TODOS los artículos de la categoría "Lifestyle"
    """
    pass
    return render(request, "category_lifestyle.html", {"posts" : []})

def category_health(request):
    """
        Muestra TODOS los artículos de la categoría "Health"
    """
    pass
    return render(request, "category_health.html", {"posts" : []})