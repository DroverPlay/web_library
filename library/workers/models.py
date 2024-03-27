from django.db import models


class Workers(models.Model):
    id = models.IntegerField('Код Работника', primary_key="True")
    surname = models.CharField('Фамилия', max_length=100)
    library_id = models.IntegerField('Код Библиотеки')
    post = models.CharField('Должность', max_length=100)
    birth_year = models.CharField('Год рождения', max_length=100)
    year_to_work = models.CharField('Год начала работы', max_length=100)
    education = models.CharField('Образование', max_length=100)
    salary = models.FloatField('Зарплата')

    def __str__(self):
        return self.surname

    class Meta:
        verbose_name = "Работник"
        verbose_name_plural = "Работники"