from .models import *
# from django import forms
from django.forms import ModelForm, TextInput, Textarea
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Логин', max_length=150)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

class UsersForm(ModelForm):
    class Meta:
        model = StandartUser
        fields = ['password', 'username', 'last_name', 'first_name']

        widgets = {
            "password": TextInput(attrs={
                'class': 'form-control'
            }),
            "username": TextInput(attrs={
                'class': 'form-control'
            }),
            "last_name": TextInput(attrs={
                'class': 'form-control'
            }),
            "first_name": TextInput(attrs={
                'class': 'form-control'
            }),
        }

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['author', 'title', 'intro', 'content']

        widgets = {
            "author": TextInput(attrs={
                'class': 'form-control'
            }),
            "title": TextInput(attrs={
                'class': 'form-control'
            }),
            "intro": TextInput(attrs={
                'class': 'form-control'
            }),
            "content": Textarea(attrs={
                'class': 'form-control'
            }),
        }

class ChannelsForm(ModelForm):
    class Meta:
        model = Channel
        fields = ['user','name']

        widgets = {
                "user": TextInput(attrs={
                    'class': 'form-control'
                }),
                "name": TextInput(attrs={
                    'class': 'form-control'
                }), 
        }

class ArticlesChannelForm(ModelForm):
    class Meta:
        model = ArticleChannel
        fields = ['title', 'intro', 'content']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control'
            }),
            "intro": TextInput(attrs={
                'class': 'form-control'
            }),
            "content": Textarea(attrs={
                'class': 'form-control'
            }),
        }


# class ArticlesChannelForm(ModelForm):
#     class Meta:
#         model = ArticleChannel
#         fields = ['channel', 'title', 'intro', 'content']

#         widgets = {
#             "channel": TextInput(attrs={
#                 'class': 'form-control'
#             }),
#             "title": TextInput(attrs={
#                 'class': 'form-control'
#             }),
#             "intro": TextInput(attrs={
#                 'class': 'form-control'
#             }),
#             "content": Textarea(attrs={
#                 'class': 'form-control'
#             }),
#         }


class WriteMessageForm(ModelForm):
    class Meta:
        model = MessageСhat
        fields = ['user','chat','content']
        widgets = {
            "user": TextInput(attrs={
                'class': 'form-control'
            }),
            "chat": TextInput(attrs={
                'class': 'form-control'
            }),
            "content": TextInput(attrs={
                'class': 'form-control'
            }),
        }

        