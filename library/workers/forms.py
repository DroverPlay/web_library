from .models import Workers
from django.forms import  ModelForm, TextInput



class WorkersForm(ModelForm):
    class Meta:
        model = Workers
        fields = ['surname', 'library_id', 'post', 'birth_year', 'year_to_work', 'education', 'salary']

        widgets = {
            'surname': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия работника'
            }),
            'library_id': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Код библиотеки'
            }),
            'post': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Должность работника'
            }),
            'education': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Образование работника'
            }),
            'birth_year': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Год рождения работника'
            }),
            'year_to_work': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Год начала работы работника'
            }),
            'salary': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Зарплата работника'
            })

        }