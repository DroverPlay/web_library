from django.db import models


class Libraries(models.Model):
    id = models.IntegerField('Код Библиотеки', primary_key="True")
    name = models.CharField('Название', max_length=100)
    adres_library = models.CharField('Адрес Библиотеки', max_length=100)
    city = models.CharField('Город', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Библиотека"
        verbose_name_plural = "Библиотеки"