from threading import local
from django.shortcuts import render,redirect,get_object_or_404
from .models import*
from .forms import bookforms,categoryforms

# Create your views here.
def index(request):
      from .models import books
      from .models import category,earn
    #  ال اف دي عشان اضافه الفئه من السيد بار 
      if request.method == 'POST':
        add_book = bookforms(request.POST,request.FILES)
      
        if add_book.is_valid():
             add_book.save()
             return redirect('index') 
        add_category=categoryforms(request.POST)
        if add_category.is_valid():
             add_category.save() 
      
     
     
      context={
        'b':books.objects.all(),
        'category':category.objects.all(),
        'form':bookforms(), 
        'formcat':categoryforms(),
        'allbooks':books.objects.filter(active=True).count(),
        'bookavailable':books.objects.filter(status='available').count(),
        'booksold':books.objects.filter(status='sold').count(),
        'bookrental':books.objects.filter(status='rental').count(),
        'earn':earn.objects.all(),
      }
      return render(request ,'pages/index.html',context)

def books(request):
      from .models import books
      from .models import category
      if request.method == 'POST':
        add_book = bookforms(request.POST,request.FILES)
        if add_book.is_valid():
             add_book.save()
             return redirect('/') 
         #  الف دي عشان اضافه الفئه من السيد بار
        add_category=categoryforms(request.POST)
        if add_category.is_valid():
             add_category.save()
      context={
        'b':books.objects.all(),
        'category':category.objects.all(),
        'form':bookforms(), 
        'formcat':categoryforms(),
      
      }
      return render(request ,'pages/books.html',context)

def update(request,id):
      from .models import books
      from .models import category
      book_id=books.objects.get(id=id)
      if request.method=='POST':
         book_save=bookforms(request.POST,request.FILES,instance=book_id)
         if book_save.is_valid():
              book_save.save()
              return redirect('/')
      else:
         book_save=bookforms(instance=book_id)
      context={
        'form':book_save,
      }   
      
      return render(request ,'pages/update.html',context)


def delete(request,id):
      from .models import books
      from .models import category

      book_delete=get_object_or_404(books,id=id)
      if request.method=='POST':
        book_delete.delete()
        return redirect('index')
      return render(request ,'pages/delete.html')



