from django.shortcuts import render
from django.template.loader import render_to_string

def index(request):
    data = {
        'title': 'Главная страница'
    }
    return render(request, 'main_page/main.html', data)

def columns(request):
    return render(request, 'main_page/info_columns.html')

def add_column(request):
    return render(request, 'main_page/add_column.html')

def about(request):
    return render(request, 'main_page/about.html')
