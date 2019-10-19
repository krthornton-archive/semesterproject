from django import forms

from .models import NewUser, Item


# form for creating a new user
class NewUserForm(forms.ModelForm):
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


# form for searching for items
class ItemSearchForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'name'
        ]