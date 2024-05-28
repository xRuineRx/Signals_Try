from django import forms
from .models import  GamePost
from ckeditor.fields import RichTextFormField

class GamePostForm(forms.ModelForm):
    class Meta:
        model = GamePost
        fields = [
            'header',
            'text',
            'CategoryCheck',
            'body',
        ]
        widgets = {
            'body': RichTextFormField(config_name='default'),
        }



