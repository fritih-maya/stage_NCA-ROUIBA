from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),          # URL de l’admin
    path('', include('rouibapp.urls')),       # Inclusion des URLs de ton app
]
