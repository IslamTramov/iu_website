from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import news_post, custom_user

class news_post_form(forms.ModelForm):
    class Meta:
        model = news_post
        fields = ('title', 'text', 'image')
        labels = {
            'title': 'Заголовок',
            'text': 'Текст',
            'image': 'Изображение',
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Заголовок', 'class': 'form-control'}),
            'text': forms.Textarea(attrs={'placeholder': 'Текст статьи', 'class': 'form-control'}),
            'image': forms.FileInput(attrs={'id': 'image_field'}),
        }


class register_form(UserCreationForm):
    class Meta:
        model = custom_user
        fields = ('username', 'password1', 'password2')

        labels = {
            'username': 'Логин',
            'password1': 'Пароль',
            'password2': 'Повторный пароль',
        }


class login_form(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
