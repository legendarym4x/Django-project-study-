from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string


menu = ['About us', 'Add article', 'Feedback', 'Sign In']


data_db = [
    {'id': 1, 'title': 'Angelina Jolie', 'content': 'Angelina Jolie Biography', 'is_published': True},
    {'id': 2, 'title': 'Margot Robbie', 'content': 'Margot Robbie Biography', 'is_published': False},
    {'id': 3, 'title': 'Julia Roberts', 'content': 'Julia Roberts Biography', 'is_published': True},
]


def index(request): # HttpRequest
    # t = render_to_string('women/index.html')
    # return HttpResponse(t)
    data = {
        'title': 'main page?',
        'menu': menu,
        'posts': data_db,
    }
    return render(request, 'women/index.html', context=data)


def about(request):
    return render(request, 'women/about.html', {'title': 'About us'})


def categories(request, cat_id):
    return HttpResponse(f'<h1>Publications by categories</h1><p>id: {cat_id}</p>')


def categories_by_slug(request, cat_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'<h1>Publications by categories</h1><p>slug: {cat_slug}</p>')


def archive(request, year):
    if year > 2023:
        uri = reverse('cats', args=('music', ))
        return redirect(uri)
    return HttpResponse(f'<h1>Archive by years</h1><p>{year}</p>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Page Not Found</p>')


