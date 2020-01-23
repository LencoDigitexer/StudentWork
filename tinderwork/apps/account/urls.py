from django.urls import path
from . import views

urlpatterns = [
    path('', views.account_index, name='index'),
    path('login/', views.login_user, name="login"),
    path('register/', views.register_user, name='register'),

]