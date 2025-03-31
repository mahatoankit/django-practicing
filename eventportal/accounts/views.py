from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
# Create your views here.


def signUpView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('eventlandingPage')
    else:
        form = UserCreationForm()

    return render(request, 'accounts/signup.html', {'form':form})


def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('eventlandingPage')
            
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})



def logoutView(request):
    logout(request)
    return redirect('login')