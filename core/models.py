from django.db import models
from django.utils import timezone


BOOKS = 1
PROGRAMMING = 2
TRAVEL = 3
CATEGORIES = (
    (BOOKS,         "Books"),
    (PROGRAMMING,   "Programming"),
    (TRAVEL,        "Travel"),
)


class Post(models.Model): 
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) 
    title = models.CharField(max_length=200) 
    category = models.SmallIntegerField(choices=CATEGORIES, default=2)
    text = models.TextField() 
    created_date = models.DateField(default=timezone.now) 
    published_date = models.DateField(blank=True, null=True) 

    def publish(self): 
        self.published_date = timezone.now() 
        self.save() 

    def __str__(self): 
        return self.title 
