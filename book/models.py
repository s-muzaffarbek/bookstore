from decimal import Decimal

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=10)
    slug = models.SlugField(max_length=10)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='author/', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    cover = models.ImageField(upload_to='book/')
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_book')
    price = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, related_name='languege_book',
                                 blank=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True, related_name='author_book')
    like = models.PositiveIntegerField(default=0)
    rating_avg = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return self.title

    @property
    def price2(self):
        return round(self.price - self.price * Decimal(0.2), 2)

class Image(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='book/image/')

    def __str__(self):
        return self.title

