from django import forms
from .models import UploadedImage, User


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedImage
        fields = ['image']

class UserLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'name': 'email', 'id': 'email', 'autocomplete': 'email', 'placeholder': 'Enter your email','class': 'appearance-none rounded-md relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm', 'required':''}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'name': 'password', 'id': 'password', 'placeholder': 'Enter your password','class': 'appearance-none rounded-md relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm', 'required':''}))

class UserRegisterForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'name': 'first_name', 'id': 'first_name', 'placeholder': 'Enter first name', 'placeholder': 'Enter your email', 'class': 'appearance-none rounded-md relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm', 'required':''}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'name': 'last_name', 'id': 'last_name', 'placeholder': 'Enter last name', 'placeholder': 'Enter your email', 'class': 'appearance-none rounded-md relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm', 'required':'false'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'name': 'email', 'id': 'email', 'autocomplete': 'email', 'placeholder': 'Enter your email', 'class': 'appearance-none rounded-md relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm', 'required':''}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'name': 'password', 'id': 'password', 'placeholder': 'Enter your password', 'class': 'appearance-none rounded-md relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm', 'required':''}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'name': 'confirm_password', 'id': 'confirm_password', 'placeholder': 'Confirm your password', 'class': 'appearance-none rounded-md relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm', 'required':''}))

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        first_name = cleaned_data.get('first_name')
        email = cleaned_data.get('email')

        if len(first_name) < 4:
            self.add_error('first_name', "First name must be at least 4 characters long")
        if password != confirm_password:
            self.add_error('confirm_password',"Passwords do not match")
        if email.lower() in User.objects.all().values_list('username', flat=True):
            self.add_error('email', "Email already exists")
        