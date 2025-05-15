from django.contrib import admin
from django.urls import path, include  # 👈 include is needed to include app URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),  # 👈 this line includes URLs from accounts app
]
