from django.contrib import admin
from django.db import models
from django.forms import Textarea

from .models import Post
from .models import Image
from .models import Code


class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':10, 'cols':80})},
    }

    # Home > Core > Posts page
    list_display = ('id', 'category', 'title', 'path', 'created_date', 'published_date', 'featured', 'enabled')
    list_filter = ('category', 'featured', 'enabled')

    # Home > Core > Posts > [specific] page
    fieldsets = (
        ('General', {'fields': ('author', 'category', 'title', 'summary', 'path', 'created_date', 'published_date')}),
        ('Availability', {'fields': ('featured', 'enabled')})
    )


class ImageAdmin(admin.ModelAdmin):
    # Home > Core > Images page
    list_display = ('id', 'post', 'image', 'summary', 'order')
    list_filter = ('post',)


class CodeAdmin(admin.ModelAdmin):
    # Home > Core > Code page
    list_display = ('id', 'post', 'language', 'order')
    list_filter = ('post', 'language')


admin.site.register(Post, PostAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Code, CodeAdmin)
