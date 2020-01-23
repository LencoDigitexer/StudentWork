from django.urls import path
from . import views

urlpatterns = [
    path('', views.dash_index, name='index'),
    path('list/', views.list_work),
]