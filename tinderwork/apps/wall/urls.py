from django.urls import path
from . import views

urlpatterns = [
    path('', views.wall_index, name='index'),
]