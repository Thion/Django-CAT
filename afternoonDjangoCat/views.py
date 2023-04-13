from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def blog(request):
    return render(request, 'blog.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def pricing(request):
    return render(request, 'pricing.html')


def services(request):
    return render(request, 'services.html')


def team(request):
    return render(request, 'team.html')


def blog_single(request):
    return render(request, 'blog-single.html')


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'Account created for{username}')
            return redirect('users-registration')
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form':form})


