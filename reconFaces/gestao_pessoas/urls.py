from django.contrib import admin
from django.urls import path, include
from pessoas import urls as pessoas_urls
from home import urls as home_urls

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', include(home_urls)),
    path('pessoas/', include(pessoas_urls)),
    path('login/', LoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


