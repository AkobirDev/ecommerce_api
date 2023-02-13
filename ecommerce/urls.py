from django.contrib import admin
from django.urls import path
from django.conf import settings, include
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/allauth', include('allauth.urls')),
    
]


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)