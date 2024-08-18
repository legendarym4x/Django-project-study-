from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string

menu = [
    {'title': "About us", 'url_name': 'about'},
    {'title': "Add article", 'url_name': 'add_page'},
    {'title': "Feedback", 'url_name': 'contact'},
    {'title': "Sign In", 'url_name': 'login'}
]

data_db = [
    {'id': 1, 'title': 'Angelina Jolie', 'content': 'Angelina Jolie Biography', 'is_published': True},
    {'id': 2, 'title': 'Margot Robbie', 'content': 'Margot Robbie Biography', 'is_published': False},
    {'id': 3, 'title': 'Julia Roberts', 'content': 'Julia Roberts Biography', 'is_published': True},
]


def index(request):  # HttpRequest
    # t = render_to_string('women/index.html')
    # return HttpResponse(t)
    data = {
        'title': 'Main page',
        'menu': menu,
        'posts': data_db,
    }
    return render(request, 'women/index.html', context=data)


def about(request):
    return render(request, 'women/about.html', {'title': 'About us', 'menu': menu})


def show_post(request, post_id):
    return HttpResponse(f'Show post with id: {post_id}')


def add_page(request):
    return HttpResponse('Add article')


def contact(request):
    return HttpResponse('Feedback')


def login(request):
    return HttpResponse('Sign In')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Page Not Found</p>')
