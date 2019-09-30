from django.shortcuts import render, HttpResponse
from django.views.decorators.http import require_http_methods

from .models import NewUser
from .forms import NewUserForm


# Create your views here.
def index(request):
    context = {}
    return render(request, 'app/home.html', context)


# view for creating new users
@require_http_methods(['GET', 'POST'])
def register(request):
    if request.method == 'GET':
        # this is a GET request, send empty form
        form = NewUserForm()
        return render(request, 'registration/register.html', {'form': form})
    elif request.method == 'POST':
        # the user is submitting a form
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = NewUser.objects.create_user(**form.cleaned_data)
            user.save()
        return index(request)
