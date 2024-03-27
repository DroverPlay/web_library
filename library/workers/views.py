from django.shortcuts import render, redirect
from .models import Workers
from .forms import WorkersForm


def workers_home(request):
    workers = Workers.objects.all()
    return render(request, 'workers/workers_home.html', {'workers': workers})

def add_workers(request):
    error = ''
    if request.method == 'POST':
        form = WorkersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('workers_home')
        else:
            error = 'Форма заполнена неправильно!'

    form = WorkersForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'workers/add_workers.html', data)