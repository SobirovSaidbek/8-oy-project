from django.contrib import admin

from bookss.models import BookModel


@admin.register(BookModel)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author',)
    search_fields = ('title', 'author',)
    list_filter = ('title',)
