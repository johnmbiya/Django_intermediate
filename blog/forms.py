from django import forms
from django.contrib.auth import get_user_model
from . import models


User = get_user_model()

class PhotoForm(forms.ModelForm):
    class Meta:
        model = models.Photo
        fields = ['image', 'caption']
        labels = {
            'image': 'Image',
            'caption': 'Légende'
        }
        help_texts = {
            'image': 'Choisissez une image',
            'caption': 'Ajoutez une légende'
        }

class BlogForm(forms.ModelForm):
    edit_blog = forms.BooleanField(widget=forms.HiddenInput, initial=False)
    class Meta:
        model = models.Blog
        fields = ['title', 'content']

class DeleteBlogForm(forms.Form):
    delete_blog = forms.BooleanField(widget=forms.HiddenInput, initial=True)

class FollowUsersForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['follows']
   