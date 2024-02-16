from django.contrib import admin
from django.urls import path
from blogpp import views
from blogpp.views import chat_room  # Импорт функции chat_room из модуля views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('admin/', admin.site.urls),
    path('chat/', chat_room, name='chat_room'),  # Использование функции chat_room из views
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
