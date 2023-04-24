# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, reverse
from .forms import SignForm, LogForm, AddLessonForm, AddGradeForm
from django.contrib.auth import login, models, logout, authenticate
from .models import CustomUser, Lesson, Grade
from django.core.exceptions import PermissionDenied


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


def user_page(request, name):
    if request.user.username != name:
        raise PermissionDenied
    user = CustomUser.objects.filter(username=name)[0]
    list_of_lessons = Lesson.objects.filter(owner=user)
    if request.method == 'POST':
         if request.POST.get('form_id') == 'delete':
             print('delete')
             Lesson.objects.get(name=request.POST.get('lesson'), owner=user).delete()
             return redirect('user_page', name=user.username)
         if request.POST.get('form_id') == 'create':
             form = AddLessonForm(request.POST)
             if form.is_valid():
                print('create')
                if len(Lesson.objects.filter(name=form.cleaned_data['name'], owner=user)) > 0:
                    form = AddLessonForm()
                    return render(request, 'user_page.html', {'user': user, 'error': 'Данный урок уже существует',
                                                              'form': form, 'lessons': list_of_lessons})
                else:
                    Lesson(name=form.cleaned_data['name'], owner=user).save()
                    form = AddLessonForm()
                    return render(request, 'user_page.html', {'user': user, 'form': form, 'lessons': list_of_lessons})
    else:
        form = AddLessonForm()
        print('render')
    return render(request, 'user_page.html', {'user':user, 'form': form, 'lessons': list_of_lessons})


def distributor(request):
    return redirect('log_in')


def lesson_page(request, name, lesson):
    if request.user.username != name:
        raise PermissionDenied
    user = CustomUser.objects.filter(username=name)[0]
    lsn = Lesson.objects.filter(name=lesson, owner=user)[0]
    notes = []
    for grade in Grade.objects.filter(lesson=lsn):
        notes.append(grade.value)
    if request.method == 'POST':
        if request.POST.get('form_id') == 'delete':
            Grade.objects.filter(lesson=lsn, value=request.POST.getlist('value')[0])[0].delete()
        if request.POST.get('form_id') == 'create':
            form = AddGradeForm(request.POST)
            if form.is_valid():
                new_grade = Grade(value=form.cleaned_data['value'], lesson=lsn)
                new_grade.save()
                notes.append(new_grade.value)
        return redirect('lesson_page', name=name, lesson=lesson)
    else:
        form = AddGradeForm()
        if notes:
            average = sum(notes)/len(notes)
        else:
            return render(request, 'lesson_page.html', {'form': form, 'lesson': lsn, 'notes': notes})
        notes.sort(reverse=True)
    return render(request, 'lesson_page.html', {'form': form, 'lesson': lsn, 'notes': notes, 'av': average})
