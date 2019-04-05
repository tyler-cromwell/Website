import enum

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
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    category = models.SmallIntegerField(choices=CHOICES, default=Category.PROGRAMMING.value)
    summary = models.CharField(max_length=40)
    text = models.TextField()
    created_date = models.DateField(default=timezone.now)
    published_date = models.DateField(blank=True, null=True)
    enabled = models.BooleanField(
        help_text='Show/hide post',
        default=False
    )
    featured = models.BooleanField(
        help_text='Pin to front page',
        default=False
    )

    def publish(self):
        self.published_date = timezone.now()
        self.enabled = True
        self.save()

    def __str__(self):
        return self.title
