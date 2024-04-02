from django.db import models


class Fund(models.Model):
    id = models.IntegerField('Код Фонда', primary_key="True")
    name = models.CharField('Название', max_length=100)
    id_library = models.IntegerField('Код Библиотеки')
    count_book = models.IntegerField('Кол-во книг')
    count_magazine = models.IntegerField('Кол-во журналов')
    count_newspaper = models.IntegerField('Кол-во газет')
    count_collection = models.IntegerField('Кол-во  сборников')
    count_dissertation = models.IntegerField('Кол-во диссертаций')
    count_report = models.IntegerField('Кол-во рефератов')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Фонд"
        verbose_name_plural = "Фонды"
