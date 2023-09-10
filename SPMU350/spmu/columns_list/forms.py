from .models import Columns
from django.forms import ModelForm, TextInput

class ColumnsForm(ModelForm):
    class Meta:
        model = Columns
        fields = ['title', 'link', 'info', 'photo']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ФИО выпускника'
            }),
            "link": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ссылка на статью в Википедии'
            }),
            "info": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Краткая информация'
            }),
            "photo": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ссылка на фото'
            }),
        }