from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('browse', views.browse_items, name='browse'),
    re_path(r'^item/(?P<slug>[a-z\-]+)/$', views.item_description, name='description'),
    path('register', views.register, name='register'),
]
