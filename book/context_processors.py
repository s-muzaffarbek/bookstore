from book.models import Category, Author, Language


def category(request):
    categories = Category.objects.all()

    return {'categories': categories}


def author(request):
    authors = Author.objects.all()

    return {'authors': authors}


def languages(request):
    languages = Language.objects.all()

    return {'languages': languages}