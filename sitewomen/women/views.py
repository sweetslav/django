from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'addpage'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'},
]


data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Lorem ipsum dolor sit amet, consetetur sadipscing '
                                                     'elitr, sed diam. nonumy eirmod tempor invidunt ut labore et '
                                                     'dolore magna aliquyam erat, sed diam voluptua. At vero eos et '
                                                     'accusam et justo duo dolores et ea rebum. Stet clita kasd '
                                                     'gubergren, no sea takimata sanctus est Lorem ipsum dolor sit '
                                                     'amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, '
                                                     'sed diam nonumy e rebum. Stet clita kasd gubergren, '
                                                     'no sea takim hendrerit in vulputate velit esse '
                                                     'molestie consequat, vel illum dolore eu feugiat nulla facilisis '
                                                     'at vero eros et accumsan et iusto odio dignissim qui blandit '
                                                     'praesent luptatum zzril delenit augue duis dolore te feugait '
                                                     'nulla facilisi.  ', 'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография', 'is_published': True},
]

cats_db = [
    {'id': 1, 'name': 'Актрисы'},
    {'id': 2, 'name': 'Певицы'},
    {'id': 3, 'name': 'Спортсменки'},
]


def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db,
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context=data)


def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте', 'menu': menu})


def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id = {post_id}')


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена :( </h1>")


def addpage(request):
    return HttpResponse('Добавление статьи')


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


def show_category(request, cat_id):
    data = {
        'title': 'Отображение по рубрикам',
        'menu': menu,
        'posts': data_db,
        'cat_selected': cat_id,
    }
    return render(request, 'women/index.html', context=data)