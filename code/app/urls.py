from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_user', views.new_user, name='new_user'),
]