# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class CustomUser(User):
    def __str__(self):
        return self.username


class Lesson(models.Model):
    name = models.CharField(max_length=20, blank=False,
                            error_messages={'max_length': 'Длина имени не должна превышать 20 символов',
                                            'blank': 'Название не должно быть пустым'})
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.name} -> {self.owner}'


class Grade(models.Model):
    value = models.FloatField(max_length=4, blank=False, error_messages={'max_length':
                                                                         'Ввод не должен быть более 4 символов',
                                                                         'blank':
                                                                         'Поле не должно быть пустым'})
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.value} -> {self.lesson}'
