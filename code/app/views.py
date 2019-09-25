from django.shortcuts import render, HttpResponse
from django.views.decorators.http import require_http_methods

from .models import NewUser
from .forms import NewUserForm


# Create your views here.
def index(request):
    return HttpResponse("hello world!")


# view for creating new users
@require_http_methods(['GET', 'POST'])
def new_user(request):
    if request.method == 'GET':
        # this is a GET request, send empty form
        form = NewUserForm()
        return render(request, 'app/new_user.html', {'form': form})
    elif request.method == 'POST':
        # the user is submitting a form
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = NewUser(**form.cleaned_data)
            user.save()
            print("DEBUG: New user created! %s" % user.username)    # debug
        return HttpResponse("User created! %s" % user.username)
