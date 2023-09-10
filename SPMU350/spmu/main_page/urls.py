from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('columns/', views.columns, name='columns'),
    path('columns/add_column/', views.add_column, name='add_column'),
    path('columns/about/', views.about, name='about'),
]
