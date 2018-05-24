from django.contrib import admin
from django.conf.urls import  url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    url('admin/', admin.site.urls),
	url(r'^books/$', views.books_list, name='books_list'),
	url(r'^videos/$', views.videos_list, name='videos_list'),

	url(r'^pictures/$', views.pictures_list, name='pictures_list'),
	url(r'^years/(?P<pk>\d+)$', views.picture_page, name='picture_page'),
	url(r'^pictures/(?P<year>\d+)$', views.year_page, name='year_page'),
	#url(r'^pictures/(?P<pk>\d+)$', views.picture_page, name='picture_page'),

	url(r'^videos/(?P<pk>\d+)$', views.video_page, name='video_page'),
    url(r'^books/(?P<pk>\d+)$', views.book_page, name='book_page'),
	url(r'^$', views.index, name='index'),

	
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
