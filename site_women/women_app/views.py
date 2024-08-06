from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse
from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]

# Create your views here.
def index(request):
    posts = Women.published.all().select_related('cat')
    data = {
        'menu': menu,
        'posts': posts,
        'cat_selected': 0,
    }
    return render(request, 'women_app/index.html', context=data)

def about(request):
    return render(request, 'women_app/about.html', context={'title': 'О сайте', 'menu': menu})

def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    data = {
        'title': post.title,
        'menu': menu,
        'post': post,
        'cat_selected': post.cat.id,
    }

    return render(request, 'women_app/post.html', context=data)

def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Women.published.filter(cat_id=category.pk).select_related('cat')
    data = {
        'title': f'Рубрика {category.name}',
        'menu': menu,
        'posts': posts,
        'cat_selected': category.pk,
    }
    return render(request, 'women_app/index.html', context=data)

def show_tag_postlist(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = tag.tags.filter(is_published=Women.Status.PUBLISHED).select_related('cat')

    data = {
        'title': f'Тэг: {tag.tag}',
        'menu': menu,
        'posts': posts,
        'cat_selected': None
    }

    return render(request, 'women_app/index.html', context=data)

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