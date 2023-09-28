
from django.contrib import admin
from django.urls import path, include 
from noticia.views import home




urlpatterns = [
    path('', home, name='home'),
    path('autor/', include('noticia.urls')),
    path('admin/', admin.site.urls),
   
]
