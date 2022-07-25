from django.db import models
from account.models import MyUser
from book.models import Book


class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_comment')
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='user_comment')
    content = models.TextField()
    rating = models.PositiveIntegerField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


class Like(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_like')
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='user_like')
    # like = models.BooleanField()

    def __str__(self):
        return self.book.title
