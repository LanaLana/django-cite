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
	years = []
	for p in pictures:
		years.append(p.year)
	years = list(set(years))
	return render(request, 'template.html', {'tab': 'pictures', 'years': years})	

def year_page(request, year):
	pictures_l = Picture.objects.all()
#	

	#pictures = Picture.objects.all(year=year)
	pictures = []
	for p in pictures_l:
		if p.year == year:
			pictures.append(p)
#
	return render(request, 'template.html', {'tab': 'year', 'pictures': pictures})	

def book_page(request, pk):
	books = Book.objects.all()
	book = Book.objects.get(pk=pk)
	return render(request, 'template.html', {'tab': 'books', 'books':books, 'book': book})

def picture_page(request, pk):
	pictures = Picture.objects.all()
	picture = Picture.objects.get(pk=pk)
	return render(request, 'template.html', {'tab': 'pictures', 'pictures':pictures, 'picture': picture})	
