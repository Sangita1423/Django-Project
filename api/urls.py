from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
	#path('admin/', admin.site.urls),
 	 
	#path('', views.HomeView.as_view()),
	# path('test-api', views.get_data),
	#path('api', views.ChartData.as_view()),
 	path('dropdown', views.showempnames),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]
