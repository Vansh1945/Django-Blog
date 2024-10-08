from django import forms
from tinymce.models import HTMLField
from .models import *


class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = [ 'content']