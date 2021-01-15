from django.contrib import admin
from myApp.models import Book
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    l = ['title', 'author', 'num','p_date','numOfCopies']


admin.site.register(Book,BookAdmin)