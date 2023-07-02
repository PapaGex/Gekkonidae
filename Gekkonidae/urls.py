from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls')),
    path('gecko/', include('geckos.urls')),
    path('api/v1/', include('geckos.urls')),
    path('', include('geckos.urls'))
]
