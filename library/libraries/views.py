from django.shortcuts import render, redirect
from .models import Libraries
from .forms import LibrariesForm


def libraries_home(request):
    libraries = Libraries.objects.all()
    return render(request, 'libraries/libraries_home.html', {'libraries': libraries})


def add_libraries(request):
    error = ''
    if request.method == 'POST':
        form = LibrariesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('libraries_home')
        else:
            error = 'Форма заполнена неправильно!'

    form = LibrariesForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'libraries/add_libraries.html', data)
