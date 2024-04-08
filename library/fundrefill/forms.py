from .models import FundRefill
from django.forms import ModelForm, TextInput, DateInput


class FundRefillForm(ModelForm):
    class Meta:
        model = FundRefill
        fields = ['fund_id', 'workers_id', 'date', 'name_source_literature', 'literature_type_id', 'publisher',
                  'publication_date', 'count_instance']

        widgets = {
            'fund_id': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Код Фонда'
            }),
            'workers_id': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Код заполняющего работника'
            }),
            'date': DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата заполнения'
            }),
            'name_source_literature': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название источника литературы'
            }),
            'literature_type_id': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Код типа литературы'
            }),
            'publisher': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Издатель'
            }),
            'publication_date': DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            }),
            'count_instance': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество экземпляров'
            })
        }


