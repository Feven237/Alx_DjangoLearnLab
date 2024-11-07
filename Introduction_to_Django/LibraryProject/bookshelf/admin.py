from django.contrib import admin
from .models import Book

admin.site.register(Book)
 ["admin.ModelAdmin"]
 ["list_filter", "author", "publication_year"]
["search_fields", "title"]

