
from urllib import response
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as alogin, logout as alogout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from qr_app.forms import ImageUploadForm, UserLoginForm, UserRegisterForm
from .models import *
from PIL import Image
import io
from django.core.files.base import ContentFile

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        passwoxrd = request.POST['password']
        username = email.lower()
        user = authenticate(username=username, password=passwoxrd)
        if user is not None:
            alogin(request, user) 
            messages.success(request, 'Login successful')  
            return redirect('home')
        else:
            messages.error(request, 'Invalid Credentials')
            return render(request,'authentications/login.html',{'form':UserLoginForm()})
    if request.user.is_authenticated:
        return redirect('home')
    
    form = UserLoginForm()
    return render(request,'authentications/login.html',{'form':form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = email.lower()
            newuser = User.objects.create_user(email=email, username=username, password=password, first_name=first_name, last_name=last_name)
            newuser.save()
            alogin(request, newuser)
            images = UploadedImage.objects.filter(user=newuser)
            messages.success(request, 'Account created successfully',{ 'images':images })
            return redirect('home')
        else:
            return render(request,'authentications/register.html',{'form':form})
    if request.user.is_authenticated:
        return redirect('home')
    form = UserRegisterForm()
    return render(request,'authentications/register.html',{'form':form})
@login_required
def logout(request):
    if request.user:
        alogout(request)
        return redirect('login')
@login_required
def home(request):
    if request.user.is_authenticated:
        # print(request.user)
        form = ImageUploadForm()
        user = request.user
        images = UploadedImage.objects.filter(user=user)
        # print(images)
        for image in images:
            print(image.image.url)
            print(image.qr_code.url)
        context = {
            'form':form,
            'images':images
        }
        return render(request,'home/index.html',context=context)
    return render(request,'home/index.html')




def compress_image(image):
    im = Image.open(image)
    im_io = io.BytesIO()  
    im.save(im_io, 'JPEG', quality=60)  
    new_image = ContentFile(im_io.getvalue(), name=image.name)
    return new_image


def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.instance)
            form.instance.user = request.user
            form.save()
            return redirect('home')
    else:
        form = ImageUploadForm()
    return render(request, 'home/upload.html', {'form': form})

def image_success(request):
    images = UploadedImage.objects.all()
    return render(request, 'home/image_success.html', {'images': images})

@login_required
def delete_confirm(request,id):
    if request.user.is_authenticated:
        image = UploadedImage.objects.get(id=id)
        return render(request, 'images/partial/delete-image-modal.html', {'image': image})
    messages.error(request, 'Something went wrong')
    return redirect('home')

@login_required
def delete_image(request,id):
    try:
        if request.user.is_authenticated:
            if request.method == 'GET':
                image = UploadedImage.objects.get(id=id)
                image.delete()
                res = HttpResponse("")
                res['HX-Redirect'] = '/'
                return res
        return redirect('login')
    except:
        messages.error(request, 'Something went wrong')
        return redirect('home')

@login_required
def swap_image_qr(request,id,swap):
    image = UploadedImage.objects.get(id=id)
    if swap == 'img':
        return HttpResponse(f"""
        <button type="button"
        hx-get = "swap-image-qr/{image.id}/qr/"
        hx-swap="innerHTML"
        hx-target="#image-{image.id}"
        hx-trigger="click"
        id="swap-button" class="absolute inline-flex items-center px-3 py-2 text-xs font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"> Show QR Code </button>
        <a href="{image.image.url}" target=_blank class='h-[50%]'>
            <img class="rounded-t-lg  w-full h-full" src="{ image.image.url }"" alt="" />
        </a>
        """)
    else:
        
        return HttpResponse(f"""
        <button type="button"
        hx-get = "swap-image-qr/{image.id}/img/"
        hx-swap="innerHTML"
        hx-target="#image-{image.id}"
        hx-trigger="click"
        id="swap-button" class="absolute inline-flex items-center px-3 py-2 text-xs font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"> Show Image </button>
        <a href="{image.qr_code.url}" target=_blank class='h-[50%]'>
            <img class="rounded-t-lg  w-full h-full m-1"  src="{ image.qr_code.url }"" alt="" />
        </a>
        """)
    
    # images = UploadedImage.objects.all()
    # for image in images:
    #     temp = image.image
    #     image.image = image.qr_code
    #     image.qr_code = temp
    #     image.save()
    # return redirect('image_success'

@login_required
def download_image(request,id,content):
    if request.user.is_authenticated:
        try:
            files = UploadedImage.objects.filter(user=request.user)
            image = UploadedImage.objects.get(id=id)
        except:
            return redirect('home')
        
        if image in files:
            if content == 'qr':
                name = image.qr_code.name.split('/')[-1]
                response = HttpResponse(image.qr_code, content_type='image/jpeg')
                response['Content-Disposition'] = f'attachment; filename={name}'

                return response
            if content == 'img':
                name = image.image.name.split('/')[-1]
                response = HttpResponse(image.image, content_type='image/jpeg')
                response['Content-Disposition'] = f'attachment; filename={name}'
                return response
        return redirect('home')
    return redirect('home')