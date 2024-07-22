from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse

cats_db = [
    {'id': 1, 'name': 'Актрисы'},
    {'id': 2, 'name': 'Певицы'},
    {'id': 3, 'name': 'Спортсменки'},
]

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]

data_db = [ {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелины Джоли', 'is_published': True},
            {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
            {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулии Робертс', 'is_published': True}, ]

# Create your views here.
def index(request):
    # return HttpResponse(render_to_string('women_app/index.html'))
    data = {
        'menu': menu,
        'posts': data_db,
        'cat_selected': 0,
    }
    return render(request, 'women_app/index.html', context=data)

def about(request):
    return render(request, 'women_app/about.html', context={'title': 'О сайте', 'menu': menu})

def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id {post_id}')

def show_category(request, cat_id):
    data = {
        'title': 'Отображение по рубрикам',
        'menu': menu,
        'posts': data_db,
        'cat_selected': cat_id,
    }
    return render(request, 'women_app/index.html', context=data)

def categories_slug(request, cat_slug):
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>')

def archive(request, year):
    if year > 2024:
        #reverse вычисляет маршрут, если для url необходимы какие-то параметры
        #у нас это 'cats/<slug:cat_slug>' - cat_slug
        uri = reverse('cats_slug', args=('music',))
        return redirect(uri)
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')

def addpage(request):
    return HttpResponse('Добавление статьи')

def contact(request):
    return HttpResponse('Наши контакты')

def login(request):
    return HttpResponse('Войти')

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')