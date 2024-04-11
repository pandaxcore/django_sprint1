from django.urls import path
from . import views


# Указываем namespace для ссылок приложения:
app_name = 'pages'


urlpatterns = [
    path('about/', views.about, name='about'),
    path('rules/', views.rules, name='rules'),
]
