from django.contrib import admin
from django.contrib.auth.models import User

from qr_app.models import UploadedImage
# from qr_app.models import User
# Register your models here.
admin.site.register(UploadedImage)
