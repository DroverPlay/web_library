from .models import LiteratureType
from django.forms import ModelForm, TextInput


class LiteratureTypeForm(ModelForm):
    class Meta:
        model = LiteratureType
        fields = ['name']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тип литературы'
            })
        }