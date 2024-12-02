from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Book, Review, Author
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def home(request):
    books = Book.objects.all()
    return render(request, 'home.html', {'books': books})

def about_us(request):
    return render(request, 'about_us.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def login_page(request):
    if request.method == 'POST':
        pass
    return render(request, 'login.html')

def logout_page(request):
    return render(request, 'logout_alert.html')

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login')
    else:
        form = UserCreationForm()
    return render(request, 'sign_up.html', {'form': form})

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    reviews = book.reviews.all()
    return render(request, 'book_detail.html', {'book': book, 'reviews': reviews})

def add_review(request, book_id):
    if request.method == 'POST':
        book = Book.objects.get(id=book_id)
        Review.objects.create(
            book=book,
            user_name=request.POST['user_name'],
            rating=request.POST['rating'],
            comment=request.POST['comment']
        )
        return HttpResponseRedirect(f'/books/{book_id}')
    return render(request, 'add_review.html')
