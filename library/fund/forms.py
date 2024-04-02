from .models import Fund
from django.forms import ModelForm, TextInput


class FundForm(ModelForm):
    class Meta:
        model = Fund
        fields = ['name', 'id_library', 'count_book', 'count_magazine', 'count_newspaper', 'count_collection',
                  'count_dissertation', 'count_report']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название Фонда'
            }),
            'id_library': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Код библиотеки'
            }),
            'count_book': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество книг'
            }),
            'count_magazine': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество журналов'
            }),
            'count_newspaper': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество газет'
            }),
            'count_collection': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество сборников'
            }),
            'count_dissertation': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество диссертаций'
            }),
            'count_report': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество рефератов'
            })
        }


