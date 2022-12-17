from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserCreate, Profile, ChangePasswordForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from book.models import Book
from .models import Order, MyUser, Basket
from django.core.exceptions import ObjectDoesNotExist



def signup(request):
    if request.method == "POST":
        form = UserCreate(data=request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('account_login')

    else:
        form = UserCreate()

    return render(request, 'register/create_account.html', {'form': form})


def account_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'register/login_page.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


def basket(request, slug):
    user = request.user
    book = get_object_or_404(Book, slug=slug)
    try:
        basket = Basket.objects.get(user=user, book=book)
        if basket:
            return redirect('basket_list')
    except ObjectDoesNotExist:
        Order.objects.create(book=book, user=request.user)

    return redirect('book_list')


def profile_edit(request, id):
    user = get_object_or_404(MyUser, id=id)
    basket = Order.objects.filter(user=user)
    form = Profile(instance=user)
    if request.method == "POST":
        form = Profile(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form,
        'product': basket,
    }

    return render(request, 'checkout.html', context)


def password_change(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    form = ChangePasswordForm(request.user)

    context = {
        'form': form,
    }

    return render(request, 'change_password.html', context)


def card_list(request):
    user = request.user
    product = Order.objects.filter(user=user)
    context = {
        'product': product,
    }
    return render(request, 'card.html', context)

