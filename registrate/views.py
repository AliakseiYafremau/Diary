from django.shortcuts import render, redirect, reverse
from .forms import LogForm, SignForm
from app.models import CustomUser
from django.contrib.auth import login, logout, models, authenticate


# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        form = SignForm(request.POST)
        if form.is_valid():
            if CustomUser.objects.filter(username=form.cleaned_data['username']).exists() or models.User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, 'sign_up.html', {"form": form, "error": 'Имя уже занято. Попробуйте другое имя'})
            else:
                new_user = CustomUser.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
                login(request, new_user)
                return redirect('user_page', new_user)
    else:
        form = SignForm()
    return render(request, 'sign_up.html', {"form": form})


def log_in(request):
    print(request.user)
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            user = CustomUser.objects.filter(username=form.cleaned_data['username'])
            if user.exists():
                login(request, user[0])
                return redirect('user_page', user[0])
            else:
                return render(request, 'log_in.html', {'form': form, 'error': 'Имя или пароль неправильный'})
    else:
        form = SignForm()
    return render(request, 'log_in.html', {"form": form})


def distributor(request):
    return redirect('log_in')
