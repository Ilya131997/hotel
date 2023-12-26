from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from . import settings

"""
    '' - начальная страница
    'users/' - страница для пользователей(регистрация, авторизация и тд)
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gostinica.urls')),
    path('users/', include('users.urls', namespace="users")),
]

# для обслуживания файлов медиа в режиме отладки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
