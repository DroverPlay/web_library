from django.shortcuts import render, redirect
from .models import LiteratureType
from .forms import LiteratureTypeForm


def literaturetype_home(request):
    literatureType = LiteratureType.objects.all()
    return render(request, 'literaturetype/literaturetype_home.html', {'literatureType': literatureType})


def add_literaturetype(request):
    error = ''
    if request.method == 'POST':
        form = LiteratureTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('literaturetype_home')
        else:
            error = 'Форма заполнена неправильно!'

    form = LiteratureTypeForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'literaturetype/add_literaturetype.html', data)
