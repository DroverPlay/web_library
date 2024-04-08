from django.shortcuts import render, redirect
from .models import FundRefill
from .forms import FundRefillForm


def fundrefill(request):
    fundrefill = FundRefill.objects.all()
    return render(request, 'fundrefill/fundrefill.html', {'fundrefill': fundrefill})


def add_fundrefill(request):
    error = ''
    if request.method == 'POST':
        form = FundRefillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fundrefill')
        else:
            error = 'Форма заполнена неправильно!'

    form = FundRefillForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'fundrefill/add_fundrefill.html', data)