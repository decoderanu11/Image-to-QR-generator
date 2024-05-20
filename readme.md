# Django Image to QR-Code

This project is a simple Django application that allows users to upload an image, compresses the uploaded image, generates a QR code for the image URL, and stores both the compressed image and the QR code.

## Features

- Image upload
- Image compression
- QR code generation for the image URL
- Image is accessable over a internet using QR-Code stored url.
- organized images along with respective QR code
- Add, Delete, View , Download etc. necessary features available.

## Installation

Follow these steps to set up and run the project on your local machine.

### Prerequisites

- Python 3.x
- AWS S3 Access Key (Data storage on cloud)


### Clone the Repository

```bash
git clone https://github.com/decoderanu11/Image-to-QR-generator.git
cd django-image-upload-compress-qr
```

### Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Set AWS keys in .env file
 # AWS_ACCESS_KEY_ID = AccessKey
 # AWS_SECRET_ACCESS_KEY = SecretKey
 # AWS_STORAGE_BUCKET_NAME = BucketName


### Setup Django Migrations

``'bash
#!/bin/bash

echo "Setting up the Django project..."

python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

echo "Setup complete. You can now run the server with 'python manage.py runserver' "
'''

### Run Django Server

``'bash
python manage.py runserver
'''

#server will start on http://127.0.0.1:8000/


## Thankyou for Visiting :- [Anurag Sharma😊](https://github.com/decoderanu11)


