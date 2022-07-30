from django.db import models
from django.contrib.auth.models import AbstractUser
from book.models import Book

class MyUser(AbstractUser):
    image = models.ImageField(upload_to='user/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=6, null=True, blank=True)

    def __str__(self):
        return self.username


class Order(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='user_order')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_order')
    status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
#
# class CardItem(Order):
#     book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_order')
#     quantity = models.PositiveIntegerField(default=0)
#
#     def __str__(self):
#         return self.book.title
#
#
# class Card(Order):
#     items = models.ManyToManyField(CardItem)
#     total_items = models.PositiveIntegerField(default=0)
#     total_price = models.FloatField(default=0.0)
#
#     def __str__(self):
#         return f"{self.user.username} - id: {self.id}"

    