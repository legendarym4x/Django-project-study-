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

data_db = [
    {'id': 1, 'title': 'Angelina Jolie', 'content': '''<h1>Angelina Jolie</h1> (born Angelina Jolie[7], formerly Jolie
     Pitt; born June 4, 1975, Los Angeles, California, USA) is an American film, television and voice actress, film 
     director, screenwriter, producer, model, and UN Goodwill Ambassador. Winner of an Academy Award, three Golden Globe
     Awards (the first actress in history to win the award three years in a row), and two Screen Actors Guild Awards.
     ''', 'is_published': True},
    {'id': 2, 'title': 'Margot Robbie', 'content': 'Margot Robbie Biography', 'is_published': False},
    {'id': 3, 'title': 'Julia Roberts', 'content': 'Julia Roberts Biography', 'is_published': True},
]


def index(request):  # HttpRequest
    posts = Women.objects.all()

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
    return HttpResponse('Add article')


def contact(request):
    return HttpResponse('Feedback')


def login(request):
    return HttpResponse('Sign In')


def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Women.published.filter(cat_id=category.pk)

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
    posts = tag.tags.filter(is_published=Women.Status.PUBLISHED)

    data = {
        'title': f"Tag: {tag.tag}",
        'menu': menu,
        'posts': posts,
        'cat_selected': None
    }

    return render(request, 'women/index.html', context=data)
