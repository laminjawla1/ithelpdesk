from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('bookticket/', views.bookticket, name='bookticket'),
    path('feedback/', views.feedback, name='feedback'),
    path('search/', views.search, name='search'),
    path('submit_feedback/', views.submit_feedback, name='submit_feedback'),
    path('submit_ticket/', views.submit_ticket, name='submit_ticket'),
    path('search_result/', views.search_result, name='search_result')
]
