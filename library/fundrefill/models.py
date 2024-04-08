from django.db import models


class FundRefill(models.Model):
    id = models.IntegerField('Код заполнения фонда', primary_key="True")
    fund_id = models.CharField('Код фонда', max_length=100)
    workers_id = models.IntegerField('Код Работника')
    date = models.DateField('Дата заполнения')
    name_source_literature = models.CharField('Название источника литературы', max_length=100)
    literature_type_id = models.IntegerField('Код типа литературы')
    publisher = models.CharField('Издатель', max_length=100)
    publication_date = models.DateField('Дата публикации')
    count_instance = models.IntegerField('Кол-во экземпляров')

    def __str__(self):
        return self.publisher

    class Meta:
        verbose_name = "Заполнение фонда"
        verbose_name_plural = "Заполнение фондов"
