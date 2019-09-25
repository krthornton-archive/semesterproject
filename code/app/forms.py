from django.forms import ModelForm, PasswordInput

from .models import NewUser


# form for creating a new user
class NewUserForm(ModelForm):
    class Meta:
        model = NewUser
        fields = [
            'username',
            'first_name',
            'last_name',
            'password',
        ]
        widgets = {
            'password': PasswordInput(),
        }
