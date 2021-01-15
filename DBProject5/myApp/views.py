from django.shortcuts import render
from myApp.models import Book
# Create your views here.
def view1(request):
    b = Book.objects.all()
    d = {'books' : b}
    return render(request,'myApp/1.html',d)
