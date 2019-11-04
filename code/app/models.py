from uuid import uuid4

from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.utils.text import slugify


# describes a user of this website
class NewUser(AbstractUser):
    address = models.TextField(blank=True)
    phone_number = models.TextField(blank=True)
    credit_card = models.TextField(blank=True)


# describes an item in inventory
class Item(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.TextField(unique=True, max_length=30, blank=False)
    slug = models.SlugField(unique=True)
    desc = models.TextField(max_length=100, blank=False)
    price = models.FloatField(default=0.00, blank=False)
    stock = models.IntegerField(default=0, blank=False)
    image = models.TextField(blank=True)

    def __str__(self):
        return "%s: %d in stock" % (self.name, self.stock)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Item, self).save(*args, **kwargs)


# describes an item that is in a user's shopping cart
class ShoppingCartItem(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user_key = models.ForeignKey(to=NewUser, on_delete=models.CASCADE)
    item_key = models.ForeignKey(to=Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, blank=False)

    class Meta:
        unique_together = ('user_key', 'item_key')

    def __str__(self):
        return "\"%s\" in %s's cart" % (self.item_key.name, self.user_key.username)
