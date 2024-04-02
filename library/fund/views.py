from django.shortcuts import render, redirect
from .models import Fund
from .forms import FundForm


def fund(request):
    fund = Fund.objects.all()
    return render(request, 'fund/fund.html', {'fund': fund})

def add_fund(request):
    error = ''
    if request.method == 'POST':
        form = FundForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fund')
        else:
            error = 'Форма заполнена неправильно!'

    form = FundForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'fund/add_fund.html', data)