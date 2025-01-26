from django.contrib import admin
from .models import Contact, Article, Category, Tag

admin.site.register(Contact)
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Tag)