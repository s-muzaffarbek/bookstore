from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.forms import ModelForm
from .models import MyUser


class UserCreate(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['username', 'password1', 'password2']


class Profile(ModelForm):
    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'username', 'email']


class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = MyUser
        fields = ['password', 'password1', 'password2']

