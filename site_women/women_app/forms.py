from django import forms
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

from .models import *


# классом лучше объявлять, только если проверка будет проводиться многократно
@deconstructible
class RussianValidator:
    ALLOWED_CHARS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщьыъэюя0123456789- '
    # сокращённое название
    code = 'russian'

    def __init__(self, message=None):
        self.message = message if message else 'Должны присутствовать только русские символы, дефис и пробел'

    def __call__(self, value, *args, **kwargs):
        if not (set(value) <= set(self.ALLOWED_CHARS)):
            raise ValidationError(self.message, code=self.code)


# forms.Form - не привязывает к определённой модели
# class AddPostForm(forms.Form):
#     title = forms.CharField(max_length=255, min_length=5,
#                             label='Заголовок',
#                             widget=forms.TextInput(attrs={'class': 'form-input'}),
#                             error_messages={
#                                 'min_length': 'Слишком короткий заголовок',
#                                 'max_length': 'Слишком длинный заголовок',
#                                 'required': 'Заголовок обязателен к заполнению',
#                             })
#     # slug = forms.SlugField(max_length=255, label='Слаг')
#     content = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}), label='Содержание')
#     is_published = forms.BooleanField(required=False, label='Опубликовать?')
#     cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label='Без категории')
#     husband = forms.ModelChoiceField(queryset=Husband.objects.all(), required=False, label='Супруг',
#                                      empty_label='Не замужем')
#
#     # только для title
#     def clean_title(self):
#         # cleaned_data возвращает словарь из прошедших проверку значений
#         title = self.cleaned_data['title']
#         ALLOWED_CHARS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщьыъэюя0123456789- '
#
#         # проверка на подмножество
#         if not (set(title) <= set(ALLOWED_CHARS)):
#             raise ValidationError('Должны присутствовать только русские символы, дефис и пробел')
#         return title

class AddPostForm(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=Category.objects.all(),
                                 label='Категория',
                                 empty_label='Без категории')
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(),
                                     required=False,
                                     label='Супруг',
                                     empty_label='Не замужем')

    class Meta:
        model = Women
        fields = ['title', 'content', 'is_published', 'cat', 'tags', 'husband']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Введите заголовок'}),
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 5, 'placeholder': 'Введите содержание'}),
            'tags': forms.CheckboxSelectMultiple(attrs={'class': 'form-select-multiple'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 50:
            raise ValidationError('Длина превышает 50 символов')
        return title

class UploadFileForm(forms.Form):
    file = forms.FileField(label='Файл')