from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('news/', views.index, name='news'),
    path('gallery/', views.index, name='gallery'),
    path('kontakt/', views.index, name='kontakt'),
]