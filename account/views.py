from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserCreate, Profile, ChangePasswordForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from book.models import Book
from .models import Order, MyUser
from django.core.exceptions import ObjectDoesNotExist

##3

from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes


# Create your views here.


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
    book = Book.objects.get(slug=slug)
    try:
        basket = Order.objects.get(book=book, user=user)
        if basket:
            return redirect('card_list')
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


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = MyUser.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "register/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com', [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("/password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="registrations/password_reset.html",
                  context={"password_reset_form": password_reset_form})