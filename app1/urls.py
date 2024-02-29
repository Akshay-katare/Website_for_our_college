from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('cmdept', views.cmdept, name='cmdept'),
    path('mbdept', views.mbdept, name='mbdept'),
    path('adept', views.adept, name='adept'),
]
