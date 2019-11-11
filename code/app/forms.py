from django import forms

from .models import NewUser, Item, ShoppingCartItem


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


# form for modifying a user
class UpdateUserInfoForm(forms.ModelForm):
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

    confirm = forms.BooleanField()



    class Meta:
        model = NewUser
        fields = (
            'address',
            'credit_card',
        )

