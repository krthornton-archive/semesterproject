from django.contrib import admin

from .models import NewUser, Item, ShoppingCartItem

# Register your models here.
admin.site.register(Item)
admin.site.register(ShoppingCartItem)
admin.site.register(NewUser)
