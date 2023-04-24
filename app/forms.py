# -*- coding: utf-8 -*-
from django import forms


class SignForm(forms.Form):
    username = forms.CharField(label='Имя аккаунта', max_length=20, error_messages={'max_length': 'Максимальное количество символов 20'})
    password = forms.CharField(label='Пароль', max_length=20, widget=forms.PasswordInput, error_messages={'max_length': 'Максимальное количество символов 20'})


class LogForm(forms.Form):
    username = forms.CharField(label='Имя аккаунта', max_length=20, error_messages={'max_length': 'Максимальное количество символов 20'})
    password = forms.CharField(label='Пароль', max_length=20, widget=forms.PasswordInput, error_messages={'max_length': 'Максимальное количество символов 20'})


class AddLessonForm(forms.Form):
    name = forms.CharField(label='Имя нового урока', max_length=20, error_messages={'max_length': 'Максимальное количество символов 20'})


class AddGradeForm(forms.Form):
    value = forms.FloatField(label='Количество баллов', error_messages={'max_length': 'Максимальное количество символов 4'})
