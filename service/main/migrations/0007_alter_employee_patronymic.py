# Generated by Django 4.1.4 on 2022-12-15 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_project_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='patronymic',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Отчество'),
        ),
    ]
