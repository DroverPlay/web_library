# Generated by Django 5.0.3 on 2024-04-01 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libraries',
            fields=[
                ('id', models.IntegerField(primary_key='True', serialize=False, verbose_name='Код Библиотеки')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('adres_library', models.CharField(max_length=100, verbose_name='Адрес Библиотеки')),
                ('city', models.CharField(max_length=100, verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Библиотека',
                'verbose_name_plural': 'Библиотеки',
            },
        ),
    ]
