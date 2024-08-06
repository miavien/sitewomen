from django import template
from django.db.models import Count

import women_app.views as views
from women_app.models import *

register = template.Library()

@register.inclusion_tag('women_app/list_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.annotate(total=Count('posts')).filter(total__gt=0)
    return {'cats': cats, 'cat_selected': cat_selected}

@register.inclusion_tag('women_app/list_tags.html')
def show_all_tags(cat_selected=0):
    return {'tags': TagPost.objects.annotate(total=Count('tags')).filter(total__gt=0)}