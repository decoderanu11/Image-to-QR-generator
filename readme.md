# Django Image to QR-Code

This project is a simple Django application that allows users to upload an image, compresses the uploaded image, generates a QR code for the image URL, and stores both the compressed image and the QR code.

## Features

- Authentication (Account authentication) login, register etc
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

```bash
 AWS_ACCESS_KEY_ID = AccessKey
 AWS_SECRET_ACCESS_KEY = SecretKey
 AWS_STORAGE_BUCKET_NAME = BucketName
```

### Setup Django Migrations

```bash
#!/bin/bash

echo "Setting up the Django project..."

python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

echo "Setup complete. You can now run the server with 'python manage.py runserver' "
```

### Run Django Server

```bash
python manage.py runserver
```

#server will start on http://127.0.0.1:8000/


## Thankyou for Visiting :- [Anurag Sharma😊](https://github.com/decoderanu11), [Linkedin](https://www.linkedin.com/in/anurag-sharma-698990100/)

### Screenshot's
- Home Page

![Screenshot 2024-05-21 181516](https://github.com/decoderanu11/Image-to-QR-generator/assets/107468645/49b4351a-a40c-4d0f-8705-66f1120a1699)

- Dynamically Qr Code
- ![Screenshot 2024-05-21 181851](https://github.com/decoderanu11/Image-to-QR-generator/assets/107468645/2b032dda-24b3-4983-88ae-3b322acfbc1c)

- User authentication
- ![Screenshot 2024-05-21 181914](https://github.com/decoderanu11/Image-to-QR-generator/assets/107468645/2b5d5ea3-3be5-4757-be36-3b9b4347258c)

- ![Screenshot 2024-05-21 181930](https://github.com/decoderanu11/Image-to-QR-generator/assets/107468645/9f31d20a-a1ca-41b3-b30b-819237098422)

- Responsive
- ![Screenshot 2024-05-21 181644](https://github.com/decoderanu11/Image-to-QR-generator/assets/107468645/97e05e16-342d-4e45-baca-2016e2ab4e32) ![Screenshot 2024-05-21 181728](https://github.com/decoderanu11/Image-to-QR-generator/assets/107468645/4345d4df-1b24-4174-af2f-6b40a55b2747)









