from django.shortcuts import render

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'

    books = Book.objects.all()

    context = {
        'books': books
    }
    return render(request, template, context)


def books_view_pub_date(request, pub_date):
    template = 'books/books_list.html'

    all_books = Book.objects.all()
    books = []
    for i in all_books:
        if str(i.pub_date) == str(pub_date):
            books.append(i)

    all_date = []
    for all_data in all_books:
        all_date.append(str(all_data.pub_date))
    all_date_no_duplicate = [*set(all_date)]
    all_date_no_duplicate.sort()

    wiw = all_date_no_duplicate.index(str(pub_date))
    previous_date = int(wiw) - 1
    next_date = int(wiw) + 1

    context = {
        'books': books,
    }

    if previous_date >= 0 and next_date <= (len(all_date_no_duplicate) - 1):
        context['previous_date'] = all_date_no_duplicate[previous_date]
        context['next_date'] = all_date_no_duplicate[next_date]
    elif previous_date < 0:
        context['next_date'] = all_date_no_duplicate[next_date]
    elif next_date > (len(all_date_no_duplicate) - 1):
        context['previous_date'] = all_date_no_duplicate[previous_date]

    return render(request, template, context)
