from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.template.loader import render_to_string

from .models import Women, Category, TagPost

menu = [
    {'title': "About us", 'url_name': 'about'},
    {'title': "Add article", 'url_name': 'add_page'},
    {'title': "Feedback", 'url_name': 'contact'},
    {'title': "Sign In", 'url_name': 'login'}
]


def index(request):
    posts = Women.published.all().select_related('cat')

    data = {
        'title': 'Main page',
        'menu': menu,
        'posts': posts,
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context=data)


def about(request):
    return render(request, 'women/about.html', {'title': 'About us', 'menu': menu})


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)
    data = {
        'title': post.title,
        'menu': menu,
        'post': post,
        'cat_selected': 1,
    }
    return render(request, 'women/post.html', data)


def add_page(request):
    return render(request, 'women/addpage.html', {'menu': menu, 'title': 'Add article'})


def contact(request):
    return HttpResponse('Feedback')


def login(request):
    return HttpResponse('Sign In')


def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Women.published.filter(cat_id=category.pk).select_related('cat')

    data = {
        'title': f'Heading: {category.name}',
        'menu': menu,
        'posts': posts,
        'cat_selected': category.pk,
    }
    return render(request, 'women/index.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Page Not Found</p>')


def show_tag_postlist(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = tag.tags.filter(is_published=Women.Status.PUBLISHED).select_related('cat')

    data = {
        'title': f"Tag: {tag.tag}",
        'menu': menu,
        'posts': posts,
        'cat_selected': None
    }

    return render(request, 'women/index.html', context=data)
