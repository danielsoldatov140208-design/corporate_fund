from django.contrib import admin
from django.urls import path

from portal import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('grants/', views.grants, name='grants'),
    path('projects/', views.projects, name='projects'),
    path('forums/', views.forums, name='forums'),
    path('partners/', views.partners, name='partners'),
    path('trustees/', views.trustees, name='trustees'),
    path('documents/', views.documents, name='documents'),
    path('news/', views.news, name='news'),
    path('contact/', views.contact, name='contact'),
    path('health/', views.health, name='health')
]
