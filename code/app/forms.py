import re

from django import forms
from django.forms import ValidationError

from .models import NewUser, Item, ShoppingCartItem


# form for creating a new user
class NewUserForm(forms.ModelForm):
    def clean_first_name(self):
        pattern = re.compile("[a-zA-Z]+$")
        if not pattern.match(self.cleaned_data['first_name']):
            raise ValidationError("Invalid first name")
        return self.cleaned_data['first_name']

    def clean_last_name(self):
        pattern = re.compile("[a-zA-Z]+$")
        if not pattern.match(self.cleaned_data['last_name']):
            raise ValidationError("Invalid last name")
        return self.cleaned_data['last_name']

    class Meta:
        model = NewUser
        fields = [
            'username',
            'first_name',
            'last_name',
            'password',
        ]
        widgets = {
            'password': forms.PasswordInput(),
        }


# form for modifying a user
class UpdateUserInfoForm(forms.ModelForm):
    def clean_credit_card(self):
        pattern = re.compile("^[0-9]{16}$")
        if not pattern.match(self.cleaned_data['credit_card']):
            if self.cleaned_data['credit_card']:
                raise ValidationError("Invalid credit card")
        return self.cleaned_data['credit_card']

    def clean_phone_number(self):
        pattern = re.compile("^[0-9]{3}[-][0-9]{3}[-][0-9]{4}$")
        if not pattern.match(self.cleaned_data['phone_number']):
            if self.cleaned_data['phone_number']:
                raise ValidationError("Invalid phone number")
        return self.cleaned_data['phone_number']

    def clean_address(self):
        pattern = re.compile("[0-9a-zA-Z# ]+$")
        if not pattern.match(self.cleaned_data['address']):
            if self.cleaned_data['address']:
                raise ValidationError("Invalid address")
        return self.cleaned_data['address']

    def clean_first_name(self):
        pattern = re.compile("[a-zA-Z]+$")
        if not pattern.match(self.cleaned_data['first_name']):
            raise ValidationError("Invalid first name")
        return self.cleaned_data['first_name']

    def clean_last_name(self):
        pattern = re.compile("[a-zA-Z]+$")
        if not pattern.match(self.cleaned_data['last_name']):
            raise ValidationError("Invalid last name")
        return self.cleaned_data['last_name']

    class Meta:
        model = NewUser
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'address',
            'phone_number',
            'credit_card',
        ]


# form for searching for items
class ItemSearchForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'name'
        ]


# form for adding an item to a shopping cart
class NewShoppingCartItemForm(forms.ModelForm):
    class Meta:
        model = ShoppingCartItem
        fields = [
            'user_key',
            'item_key',
            'quantity',
        ]


# form for removing an item from a shopping cart
class RemoveCartItemForm(forms.ModelForm):
    class Meta:
        model = ShoppingCartItem
        fields = [
            'user_key',
            'item_key',
        ]


# form for confirming that a user wants to checkout
class ConfirmCheckoutForm(forms.ModelForm):
    def clean_credit_card(self):
        pattern = re.compile("^[0-9]{16}$")
        if not pattern.match(self.cleaned_data['credit_card']):
            raise ValidationError("Invalid credit card")
        return self.cleaned_data['credit_card']

    def clean_address(self):
        pattern = re.compile("[0-9a-zA-Z# ]+$")
        if not pattern.match(self.cleaned_data['address']):
            raise ValidationError("Invalid address")
        return self.cleaned_data['address']

    class Meta:
        model = NewUser
        fields = [
            'address',
            'credit_card',
        ]
