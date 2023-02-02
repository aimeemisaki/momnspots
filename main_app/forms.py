from django import forms
from .models import *
from django.forms.models import inlineformset_factory



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('shop_name', 'img', 'story', 'category', 'neighborhood')
        