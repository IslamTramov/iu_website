from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import news_post, custom_user

class news_post_form(forms.ModelForm):
    class Meta:
        model = news_post
        fields = '__all__'
        labels = {
            'id': 'ID',
            'title': 'Заголовок',
            'text': 'Текст',
            'image': 'Изображение',
            'author_id': 'Автор',
            'creation_date': 'Дата создания',
        }
        widgets = {
            'id': forms.TextInput(attrs={'placeholder': 'id', 'class': 'form-control'}),
            'title': forms.TextInput(attrs={'placeholder': 'Заголовок', 'class': 'form-control'}),
            'text': forms.TextInput(attrs={'placeholder': 'Текст статьи', 'class': 'form-control'}),
            'image': forms.FileInput(attrs={'id': 'image_field'}),
            'author_id': forms.TextInput(attrs={'placeholder': 'Автор', 'class': 'form-control'}),
            'creation_date': forms.DateTimeInput(attrs={'placeholder': 'test_placeholder', 'class': 'form-control'}),
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
