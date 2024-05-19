from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('tinymce/', include('tinymce.urls')),
]
