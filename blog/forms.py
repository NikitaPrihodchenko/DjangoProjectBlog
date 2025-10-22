from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment, Subscriber


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('slug', 'published_date', 'auther')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Ваш коментар...'}),
        }


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введіть ваш email...'})
        }


# class RegisterForm(UserCreationForm):
#     phone = forms.CharField(max_length=20, required=False)
#     city = forms.CharField(max_length=100, required=False)
#     birth_date = forms.DateTimeField(null=True, required=False)
#     avatar = forms.URLField(null=True, required=False)
#
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'first_name', 'last_name', 'phone', 'city', 'birth_date', 'avatar')
