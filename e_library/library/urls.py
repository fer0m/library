from django.urls import path

from . import views

# app_name = 'library'

urlpatterns = [
    path('', views.main_page, name='main'),
    path('search/', views.search_book, name='search'),
    path('detail/<int:book_id>/', views.book_info, name='detail')
]