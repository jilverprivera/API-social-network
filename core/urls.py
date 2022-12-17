from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from .views import HomeView, ProfileView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", HomeView.as_view(), name="home"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("courses/", include('apps.courses.urls')),
    path("api/v1/", include('apps.category.api.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
