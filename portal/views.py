from django.shortcuts import render

PAGES = {
    'about': 'О фонде',
    'grants': 'Гранты студентам',
    'projects': 'Проекты',
    'forums': 'Форумы и события',
    'partners': 'Партнёры',
    'documents': 'Документы',
    'news': 'Новости',
    'contact': 'Контакты',
}


def home(request):
    return render(request, 'home.html', {'page_slug': 'home'})


def page(request, slug):
    return render(
        request,
        'page.html',
        {
            'slug': slug,
            'page_name': PAGES[slug],
            'page_slug': slug,
            'page_number': str(list(PAGES).index(slug) + 1).zfill(2),
        },
    )


def about(request):
    return page(request, 'about')


def grants(request):
    return page(request, 'grants')


def projects(request):
    return page(request, 'projects')


def forums(request):
    return page(request, 'forums')


def partners(request):
    return page(request, 'partners')


def documents(request):
    return page(request, 'documents')


def news(request):
    return page(request, 'news')


def contact(request):
    return page(request, 'contact')
