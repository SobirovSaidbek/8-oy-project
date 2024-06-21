from django.db import models


class BookModel(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13)
    subtitle = models.CharField(max_length=255)
    pages = models.CharField(max_length=255)
    in_stock = models.BooleanField(default=False)
    content = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Bookss'