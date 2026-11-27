from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from portal.models import News,Document

PAGES = {
    'about': 'О фонде',
    'grants': 'Гранты студентам',
    'projects': 'Проекты',
    'courses': 'Курсы',
    'forums': 'Форумы и события',
    'partners': 'Сотрудничество',
    'trustees': 'Попечительский совет',
    'documents': 'Документы',
    'news': 'Новости',
    'contact': 'Контакты',
}


def home(request):
    latest_news = News.objects.filter(is_published=True).order_by('-created_at')[:4]
    return render(request, 'home.html', {'page_slug': 'home', 'latest_news': latest_news})


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


def courses(request):
    return page(request, 'courses')


def forums(request):
    return page(request, 'forums')


def partners(request,):
    return page(request, 'partners')


def trustees(request):
    return page(request, 'trustees')


def documents(request):
    documents = Document.objects.filter(is_published=True).order_by("-created_at")
    return page(request, 'documents',{"documents":documents})


def news(request):
    articles = News.objects.filter(is_published=True).order_by("-created_at")
    return page(request, 'news',{"articles":articles})


def news_detail(request, pk):
    article = get_object_or_404(News, pk=pk, is_published=True)
    return render(request, 'news_detail.html', {
        'article': article,
        'page_slug': 'news-detail',
    })


def contact(request):
    return page(request, 'contact')

def health(request):
    return JsonResponse({"status":"ok"})
