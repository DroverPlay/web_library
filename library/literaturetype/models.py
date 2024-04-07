from django.db import models


class LiteratureType(models.Model):
    id = models.IntegerField('Код типа литературы', primary_key="True")
    name = models.CharField('Название типа литературы', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип литературы"
        verbose_name_plural = "Типы литературы"