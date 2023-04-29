# -*- coding: utf-8 -*-
from django import forms


class AddLessonForm(forms.Form):
    name = forms.CharField(label='Имя нового урока', max_length=20, error_messages={'max_length': 'Максимальное количество символов 20'})


class AddGradeForm(forms.Form):
    value = forms.FloatField(label='Количество баллов', error_messages={'max_length': 'Максимальное количество символов 4'})
