import enum

from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


class Category(enum.Enum):
    BOOKS = 1
    PROGRAMMING = 2
    TRAVEL = 3

CHOICES = (
    (Category.BOOKS.value,        "Books"),
    (Category.PROGRAMMING.value,  "Programming"),
    (Category.TRAVEL.value,       "Travel"),
)


class Post(models.Model):
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    category = models.SmallIntegerField(
        choices=CHOICES,
        default=Category.PROGRAMMING.value
    )

    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateField(default=timezone.now)
    published_date = models.DateField(blank=True, null=True)

    featured = models.BooleanField(
        help_text='Distinguish from others',
        default=False
    )
    enabled = models.BooleanField(
        help_text='Show/hide post',
        default=False
    )

    def __str__(self):
        return self.title


class Image(models.Model):
    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE
    )
    image = models.CharField(
        help_text='Relative path name of the file',
        max_length=100
    )
    order = models.IntegerField(
        default=0,
        help_text='Order of appearance on page (descending)'
    )

    def __str__(self):
        return self.image


class Code(models.Model):
    class Meta:
        verbose_name = 'Source Code'
        verbose_name_plural = 'Source Code'

    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE
    )
    language = models.CharField(
        blank=False,
        max_length=40
    )
    order = models.IntegerField(
        default=0,
        help_text='Order of appearance on page (descending)'
    )

    text = models.TextField()
