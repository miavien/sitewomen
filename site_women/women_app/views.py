from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse
from .models import *
from .forms import *
import uuid

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


# функция-обработчик загрузки файлов
def handle_uploaded_file(f):
    postfix = str(uuid.uuid4())
    with open(f"uploads/{f.name}_{postfix}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)


# здесь вызываем обработчик и достаём из реквеста наш файл
def about(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(form.cleaned_data['file'])
    else:
        form = UploadFileForm()
    return render(request, 'women_app/about.html',
                  context={'title': 'О сайте', 'menu': menu, 'form': form})


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
        # reverse вычисляет маршрут, если для url необходимы какие-то параметры
        # у нас это 'cats/<slug:cat_slug>' - cat_slug
        uri = reverse('cats_slug', args=('music',))
        return redirect(uri)
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')


def custom_slugify(value):
    return slugify(unidecode(value))


def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            # try:
            #     form.cleaned_data['slug'] = custom_slugify(form.cleaned_data['title'])
            #     Women.objects.create(**form.cleaned_data)
            #     return redirect('home')
            # except:
            #     form.add_error(None, 'Ошибка добавления статьи')
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()

    data = {
        'menu': menu,
        'title': 'Добавление статьи',
        'form': form
    }

    return render(request, 'women_app/add_page.html',
                  context=data)


def contact(request):
    return HttpResponse('Наши контакты')


def login(request):
    return HttpResponse('Войти')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
