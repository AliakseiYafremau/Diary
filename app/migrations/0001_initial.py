# Generated by Django 4.1.6 on 2023-04-08 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(error_messages={'blank': 'Имя не должно быть пустым', 'max_lenghth': 'Длина имени не должна превышать 20 символов', 'unique': 'Имя уже занято. Введите другое'}, max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(error_messages={'blank': 'Название не должно быть пустым', 'max_lenghth': 'Длина имени не должна превышать 20 символов', 'unique': 'Такой урок уже есть. Введите другое название'}, max_length=20, unique=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.users')),
            ],
        ),
    ]
