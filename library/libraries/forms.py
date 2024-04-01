from .models import Libraries
from django.forms import ModelForm, TextInput



class LibrariesForm(ModelForm):
    class Meta:
        model = Libraries
        fields = ['name', 'adres_library', 'city']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название библиотеки'
            }),
            'adres_library': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес библиотеки'
            }),
            'city': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Город библиотеки'
            })
        }