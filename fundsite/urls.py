from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from portal import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('grants/', views.grants, name='grants'),
    path('projects/', views.projects, name='projects'),
    path('courses/', views.courses, name='courses'),
    path('forums/', views.forums, name='forums'),
    path('partners/', views.partners, name='partners'),
    path('trustees/', views.trustees, name='trustees'),
    path('documents/', views.documents, name='documents'),
    path('news/', views.news, name='news'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
    path('contact/', views.contact, name='contact'),
    path('health/', views.health, name='health')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)