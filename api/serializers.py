from django.contrib import admin

from .models import Books, Journal, BookEntity

admin.site.register(Books)
admin.site.register(Journal)
admin.site.register(BookEntity)
