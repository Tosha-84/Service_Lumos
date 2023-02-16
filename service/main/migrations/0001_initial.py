# Generated by Django 4.1.4 on 2022-12-11 17:53

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=12, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')])),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('surname', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=30, verbose_name='Отчество')),
                ('login', models.CharField(blank=True, max_length=30, null=True, unique=True, verbose_name='Логин')),
                ('password', models.CharField(blank=True, max_length=30, null=True, verbose_name='Пароль')),
                ('vk_link', models.SlugField(max_length=30, null=True, verbose_name='Ссылка на Вк')),
                ('telegram_link', models.SlugField(blank=True, max_length=30, null=True, verbose_name='Пароль')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Аватарка')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(verbose_name='Дата и время')),
                ('place', models.CharField(max_length=60, verbose_name='Адрес')),
                ('customer', models.CharField(max_length=50, verbose_name='ФИО Заказчика')),
                ('phone', models.CharField(max_length=12, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')])),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('realization', models.BooleanField(blank=True, null=True)),
                ('employee', models.ManyToManyField(related_name='Order_Employee', to='main.employee', verbose_name='Работники')),
            ],
        ),
        migrations.CreateModel(
            name='Props',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('state', models.BooleanField(default=True, verbose_name='Состояние')),
                ('comment', models.BooleanField(blank=True, null=True, verbose_name='Комментарий')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('start_date', models.DateField(default=datetime.date(2022, 12, 12), verbose_name='Дата начала')),
                ('end_date', models.DateField(default=datetime.date(2022, 12, 12), verbose_name='Дата окончания')),
                ('employee', models.ManyToManyField(related_name='Task_Employee', to='main.employee', verbose_name='Ответственные')),
                ('major', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.employee', verbose_name='Назначивший')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
                ('base_cost', models.SmallIntegerField(verbose_name='Стоимость')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Аватарка')),
                ('employee', models.ManyToManyField(related_name='Project_Employee', to='main.employee', verbose_name='Сотрудники')),
                ('order', models.ManyToManyField(related_name='Project_Order', to='main.order', verbose_name='Заказы')),
                ('props', models.ManyToManyField(related_name='Project_Props', to='main.props', verbose_name='Реквизит')),
                ('task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Project_Task', to='main.task', verbose_name='Задачи')),
            ],
        ),
    ]
