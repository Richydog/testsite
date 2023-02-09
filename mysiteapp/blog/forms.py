from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import Textarea
from django_ckeditor_5.widgets import CKEditor5Widget

from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Comments
from blog.models import Post, Profile


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', help_text='Максимум 150 символов',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', help_text='Не менее 8 символов,не только цифры',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class NewsForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['title', 'slug', 'content', 'author', 'photo', 'category', 'tags']

    widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        'slug': forms.TextInput(attrs={'class': 'form-control'}),
        'author': forms.TextInput(attrs={'class': 'form-control'}),
        'category': forms.Select(attrs={'class': 'form-control'}),
    }


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email']
        #    username = forms.CharField(label='Имя пользователя', help_text='Максимум 150 символов',
        #                              widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))

        email = forms.EmailField(label='E-mail',
                                 widget=forms.EmailInput(attrs={'class': 'form-control', 'readonly': 'True'}, ))


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('text',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields['text'].widget = Textarea(attrs={'rows': 5})
