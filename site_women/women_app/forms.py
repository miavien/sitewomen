from django import forms
from .models import *

# forms.Form - не привязывает к определённой модели
class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, label='Заголовок')
    slug = forms.SlugField(max_length=255, label='Слаг')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}), label='Содержание')
    is_published = forms.BooleanField(required=False, label='Опубликовать?')
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label='Без категории')
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(), required=False, label='Супруг', empty_label='Не замужем')

