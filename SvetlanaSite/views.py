from django.shortcuts import render
from .models import Book
from .models import Video
from .models import Picture

def index(request):
    return render(request, 'template.html', {'tab': 'homepage'})
	
def books_list(request):
	books = Book.objects.all()
	return render(request, 'template.html', {'tab': 'books', 'books': books})

def videos_list(request):
    videos = Video.objects.all()
    return render(request, 'template.html', {'tab': 'videos', 'videos': videos, 'video': None})

def video_page(request, pk):
	videos = Video.objects.all()
	video = Video.objects.get(pk=pk)
	return render(request, 'template.html', {'tab': 'videos', 'videos': videos, 'video': video})

def pictures_list(request):
	pictures = Picture.objects.all()
	return render(request, 'template.html', {'tab': 'pictures', 'pictures': pictures})

#def year2017(request):
#	pictures = Picture.objects.all()
#	return render(request, 'template.html', {'tab': 'year2017', 'pictures': pictures})	

#def year2018(request):
#	pictures = Picture.objects.all()
#	return render(request, 'template.html', {'tab': 'year2017', 'pictures': pictures})	

def book_page(request, pk):
	books = Book.objects.all()
	book = Book.objects.get(pk=pk)
	return render(request, 'template.html', {'tab': 'books', 'books':books, 'book': book})

def picture_page(request, pk):
	pictures = Picture.objects.all()
	picture = Picture.objects.get(pk=pk)
	return render(request, 'template.html', {'tab': 'pictures', 'pictures':pictures, 'picture': picture})	
