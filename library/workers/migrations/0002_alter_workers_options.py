# Generated by Django 5.0.3 on 2024-04-01 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='workers',
            options={'verbose_name': 'Работник', 'verbose_name_plural': 'Работники'},
        ),
    ]
