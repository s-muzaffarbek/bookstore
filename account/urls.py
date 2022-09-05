from django.urls import path
from .views import account_login, password_change, signup, logout_view, profile_edit, basket, card_list

urlpatterns = [
    path('login/',account_login, name='account_login'),
    path('create/',signup, name='signup'),
    path('logout/',logout_view, name='logout'),
    path('checkout/<int:id>', profile_edit, name='chek'),
    path('basket/<slug:slug>', basket, name='basket'),
    path('change-password/', password_change, name='change_password'),
    path('card-list/', card_list, name='card_list'),
]