from django.contrib import admin
from django.urls import include, path
from qr_app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('qr_app.urls')),
]
