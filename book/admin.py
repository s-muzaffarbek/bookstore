from django.contrib import admin
from .models import Book, Author, Category, Language, Image

# Register your models here.


@admin.register(Author)
class BookAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'slug']
    search_fields = ('first_name',)
    prepopulated_fields = {'slug': ('first_name', 'last_name')}


@admin.register(Category)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class ImageInline(admin.TabularInline):
    model = Image


@admin.register(Language)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


admin.site.register(Image)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)
    inlines = [ImageInline]