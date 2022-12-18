from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def index(request):
    template = 'posts/index.html'
    title = 'Yatube'
    context = {
        # В словарь можно передать переменную
        'title': title,
        # А можно сразу записать значение в словарь. Но обычно так не делают
        'text': 'Это главная страница проекта Yatube',
    }
    return render(request, template, context)


def group_list(request):
    template = 'posts/group_list.html'
    title = 'Yatube группы'
    context = {
        # В словарь можно передать переменную
        'title': title,
        # А можно сразу записать значение в словарь. Но обычно так не делают
        'text': 'Здесь будет информация о группах проекта Yatube',
    }
    return render(request, template, context)
