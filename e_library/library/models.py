from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    register_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    objects = None
    book_name = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    is_free = models.BooleanField(default=True)
    reserve_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    book_cover = models.ImageField(blank=True, upload_to='book_covers', default="book_covers/default_image.jpg")

    def __str__(self):
        return self.book_name
