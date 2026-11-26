from django.shortcuts import render
from django.http import JsonResponse
from portal.models import News

PAGES = {
    'about': 'О фонде',
    'grants': 'Гранты студентам',
    'projects': 'Проекты',
    'forums': 'Форумы и события',
    'partners': 'Сотрудничество',
    'trustees': 'Попечительский совет',
    'documents': 'Документы',
    'news': 'Новости',
    'contact': 'Контакты',
}


def home(request):
    return render(request, 'home.html', {'page_slug': 'home'})


def page(request, slug, extra_context=None):
    context = {
            'slug': slug,
            'page_name': PAGES[slug],
            'page_slug': slug,
            'page_number': str(list(PAGES).index(slug) + 1).zfill(2),
            }
    if extra_context:
        context.update(extra_context)
    return render(request,'page.html', context)


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


def trustees(request):
    return page(request, 'trustees')


def documents(request):
    return page(request, 'documents')


def news(request):
    articles = News.objects.filter(is_published=True)
    return page(request, 'news',{"articles":articles})


def contact(request):
    return page(request, 'contact')

def health(request):
    return JsonResponse({"status":"ok"})