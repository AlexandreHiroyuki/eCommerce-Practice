from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ContactForm, LoginForm, RegisterForm


def home_page(request):
    context = {
        'premium_content': 'Commoner!'
    }
    if request.user.is_authenticated:
        context['premium_content'] = 'You have privileges!'
    return render(request, 'home_page.html', context)


def contact_page(request):
    contact_form = ContactForm()
    context = {
        'form': contact_form,
    }
    return render(request, 'contact/view.html', context)


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        print("User is logged in:", request.user.is_authenticated)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            print('Error')
        context['form'] = LoginForm()
    return render(request, 'auth/login.html', context)


User = get_user_model()


def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        new_user = User.objects.create_user(username, email, password)
    return render(request, 'auth/register.html', context)
