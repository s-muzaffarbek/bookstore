from django.forms import model_to_dict
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Image, Author, Language, Category
from django.core.paginator import EmptyPage, Paginator
from comment.models import Comment, Like
from comment.forms import CommentForm
# Create your views here.

from django.http import JsonResponse


def home_list(request):
    rating_product = Book.objects.order_by('-rating_avg')[:3]
    last_product = Book.objects.order_by('-create_at')[:4]
    like_product = Book.objects.order_by('-like')


    context = {
        'rating_product': rating_product,
        'last_product': last_product,
        'like_product': like_product,
    }
    return render(request, 'home.html',context)

def search(request):
    text = request.GET.get('text', '')
    if text in text!= '':
        natija = Book.objects.filter(title__contains=text).all()[:3]
    else:
        natija = None
    context = {
        'text': text,
        'natija': natija,

    }
    return render(request, 'header.html', context)


def book_list(request):
    ordering = request.GET.get('ordering')
    if ordering:
        books = Book.objects.all().order_by(ordering)
    else:
        books = Book.objects.all()

    paginator = Paginator(books, 3)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
    except EmptyPage:
        page_obj = paginator.get_page(1)

    context = {
        'books': page_obj,
        'range': range(1, 6)
    }

    return render(request, 'book_list.html', context)


def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    comment_rating = Comment.objects.filter(book=book)
    book_categories = Book.objects.filter(category=book.category)
    summa = 0
    k = 0
    for i in comment_rating:
        summa += i.rating
        k += 1
    try:
        avg_summa = round(summa / k)
    except ZeroDivisionError:
        avg_summa = 0
    book.rating_avg = avg_summa
    book.save()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            rating = int(request.POST.get('rating'))
            com = Comment(book=book, user=request.user, text=text, rating=rating)
            com.save()
            return JsonResponse({'comment': model_to_dict(com)}, status=200)
        else:
            return redirect('book_detail', book.slug)
    else:
        form = CommentForm()

    context = {
        'book': book,
        'form': form,
        'range': range(1, 6),
        'book_categories': book_categories,
    }

    return render(request, 'book_detail.html', context)


def like(request, slug):
    user = request.user
    book = Book.objects.get(slug=slug)
    current_like = book.like

    liked = Like.objects.filter(user=user, book=book).count()

    if not liked:
        like = Like(user=user, book=book)
        like.save()
        current_like += 1
    else:
        likedd = Like.objects.filter(user=user, book=book)
        likedd.delete()
        current_like -= 1

    book.like = current_like
    book.save()

    return redirect('detail', book.slug)



def likes(request):
    if request.POST.get('action') == 'post':
        slug = request.POST.get('book_slug')
        user = request.user
        book = Book.objects.get(slug=slug)
        current_like = book.like
        liked = Like.objects.filter(user=user, book=book).count()

        if not liked:
            Like.objects.create(user=user, book=book)
            current_like += 1
        else:
            like = Like.objects.filter(user=user, book=book)
            like.delete()
            current_like -= 1
        book.like = current_like
        book.save()

        return JsonResponse({'book_likes': current_like, })


def author_books(request, slug):
    author = Author.objects.get(slug=slug)
    books = Book.objects.filter(author=author)

    context = {
        'author': author,
        'books': books,
        'range': range(1, 6),
    }

    return render(request, 'filter_books.html', context)


def language_books(request, slug):
    language = Language.objects.get(slug=slug)
    books = Book.objects.filter(language=language)

    context = {
        'language': language,
        'books': books,
        'range': range(1, 6),
    }

    return render(request, 'filter_books.html', context)


def category_books(request, slug):
    category = Category.objects.get(slug=slug)
    books = Book.objects.filter(category=category)

    context = {
        'books': books,
        'category': category,
        'range': range(1, 6),
    }

    return render(request, 'filter_books.html', context)



