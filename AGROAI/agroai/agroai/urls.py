from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from chat.views import home, login_view, logout_view, register_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('chat/', include('chat.urls')),
    path('data/', include('data.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)