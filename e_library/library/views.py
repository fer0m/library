from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from .models import Book, User


def main_page(request):
    book_list = Book.objects.all()
    paginator = Paginator(book_list, 15)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'library/main.html', {'page_obj': page_obj})


def book_info(request, book_id):
    book_object = get_object_or_404(Book, pk=book_id)

    if not book_object.is_free:
        reserve_user_name = User.objects.filter(pk=book_object.reserve_user_id)
    else:
        reserve_user_name = "free"

    return render(request, 'library/detail.html', {'book_info': book_object, 'reserve_user_name': reserve_user_name})


def search_book(request):
    query = request.GET.get('q')
    book_list = Book.objects.filter(book_name__icontains=query)
    paginator = Paginator(book_list, 15)
    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)
    return render(request, 'library/search.html', {'page_obj': page_obj, 'search_string': query})