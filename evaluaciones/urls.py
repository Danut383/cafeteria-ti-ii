from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cafeteria-norte/', views.cafeteria_norte, name='cafeteria_norte'),
    path('cafeteria-sur/', views.cafeteria_sur, name='cafeteria_sur'),
]
