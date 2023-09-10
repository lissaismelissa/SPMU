from django.shortcuts import render, redirect
from .models import Columns
from .forms import ColumnsForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.core.paginator import Paginator
from django.db.models import Q

def columns_list_home(request):
    search_query = request.GET.get('search', '')

    if search_query:
        cols = Columns.objects.filter(Q(title__icontains=search_query) | Q(info__icontains=search_query))
    else:
        cols = Columns.objects.order_by('title')

    paginator = Paginator(cols, 5)

    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url
    }

    return render(request, 'columns_list/columns_list.html', context=context)


class ColumsDetailView(DetailView):
    model = Columns
    template_name = 'columns_list/details_view.html'
    context_object_name = 'column'

class ColumsUpdateView(UpdateView):
    model = Columns
    template_name = 'columns_list/create.html'

    form_class = ColumnsForm

class ColumsDeleteView(DeleteView):
    model = Columns
    success_url = '/columns_list/'
    template_name = 'columns_list/column_delete.html'

def create(request):
    error = ''
    if request.method == 'POST':
        form = ColumnsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной. Возможно в базе данных уже существует этот человек.'

    form = ColumnsForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'columns_list/create.html', data)
