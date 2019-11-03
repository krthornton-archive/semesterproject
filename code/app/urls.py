from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('browse', views.browse_items, name='browse'),
    re_path(r'^item/(?P<slug>[a-z\-0-9]+)/$', views.item_description, name='description'),
    path('add_to_cart', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart', views.remove_from_cart, name='remove-from-cart'),
    path('view_account', views.view_account, name='view_account'),
    path('update_account', views.update_account_info, name='update_account'),
    path('change_password', views.change_password, name='change_password'),
    path('register', views.register, name='register'),
]
