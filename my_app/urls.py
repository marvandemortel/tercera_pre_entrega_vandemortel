from django.urls import path, include
from .views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('category/all', category, name="category-all"),
    path('category/beauty', category_beauty, name="category-beauty"),
    path('category/inspiration', category_inspiration, name="category-inspiration"),
    path('category/lifestyle', category_lifestyle, name="category-lifestyle"),
    path('category/health', category_health, name="category-health"),
]
