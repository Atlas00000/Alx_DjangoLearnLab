from django.contrib import admin
from django.urls import path, include  # Include is needed to link app URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Connects the `api` app
]
