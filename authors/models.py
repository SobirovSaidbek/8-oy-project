from django.db import models


class AuthorModel(models.Model):
    first_name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=155)
    email = models.EmailField()
    phone_number = models.CharField(max_length=13)
    age = models.SmallIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
