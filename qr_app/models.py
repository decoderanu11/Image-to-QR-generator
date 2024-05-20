from django.db import models
from django.core.files.base import ContentFile
import qrcode
from io import BytesIO
from PIL import Image
import os
from django.contrib.auth.models import User
import uuid
import base64


def get_a_uuid():
    uuid_id = uuid.uuid4()
    short_id = str(uuid_id)[:8]
    return short_id.replace('=', '')


class UploadedImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    
    def save(self, *args, **kwargs):
        # print(self.id)
        # Compress the image
        img = Image.open(self.image)
        img_io = BytesIO()
        foramt = img.format
        if foramt == 'PNG':
            img.save(img_io, format='PNG', quality=60)
        else:
            img.save(img_io, format='JPEG', quality=60)
        img_content = ContentFile(img_io.getvalue(), name=self.image.name)
        self.image.save(f"{str(self.user)}/{get_a_uuid()}-{self.image.name}", img_content, save=False)
        
        # Generate QR code
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr.add_data(self.image.url)
        qr.make(fit=True)
        
        qr_img = qr.make_image(fill='black', back_color='white')
        qr_io = BytesIO()
        qr_img.save(qr_io, format='PNG')
        qr_content = ContentFile(qr_io.getvalue(), name=f'{os.path.splitext(self.image.name)[0]}_qr.png')
        self.qr_code.save(qr_content.name, qr_content, save=False)
        
        super().save(*args, **kwargs)