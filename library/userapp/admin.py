from django.contrib import admin
from .models import book_table,pen_table
# Register your models here.
admin.site.register(book_table)
admin.site.register(pen_table)