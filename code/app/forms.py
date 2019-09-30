from django import forms

from .models import NewUser


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
