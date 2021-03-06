from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings

from .forms import RegisterForm
# Create your views here.

def register(request):
    template_name = 'accounts/register.html'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=user.username, password = form.cleaned_data['password1']
            )
            return redirect('core:home')
    else:
        form = RegisterForm()
    context = {'form': form}
    return render(request, template_name, context)
