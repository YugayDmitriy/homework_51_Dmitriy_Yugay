from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='webapp-home'),
    path('cats_stats', views.cats_stats),
]