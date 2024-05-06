from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('inputpage/', include('inputpage.urls')),
    path('admin/', admin.site.urls),
]
