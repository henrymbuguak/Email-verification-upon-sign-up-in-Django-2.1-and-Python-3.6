from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('user_account.urls')),
    path('admin/', admin.site.urls),
]
