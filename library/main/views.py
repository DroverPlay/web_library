from django.shortcuts import render

def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['Some', 'Hello', 'One'],
        'obj': {
            'car': 'BMW',
            'age': 18,
            'hobby': 'Football'
        }
    }
    return render(request, 'main/index.html', data)