from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):
    context = {
        'title': 'Home',
        'content': "Furniture store HOME",
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - About Us',
        'content': "About Us",
        'text_on_page': "We are a very cool store, sometimes we do it ourselves why we are so cool)"
    }

    return render(request, 'main/about.html', context)
