from django.contrib import admin
from django.urls import include, path
from qr_app.views import *
urlpatterns = [
    path('',home,name='home'),
    path('logout/',logout,name='logout'),
    path('login/',login,name='login'),
    path('register/',register,name='register'),
    path('upload/', upload_image, name='upload_image'),
    path('success/', image_success, name='image_success'),
    path('swap-image-qr/<int:id>/<str:swap>/', swap_image_qr, name='swap_image_qr'),
    path('download/<int:id>/<str:content>', download_image, name='download'),
    path('delete/<int:id>/', delete_image, name='delete_image'),
    path('delete-confirm/<int:id>/', delete_confirm, name='delete_confirm'),
]
