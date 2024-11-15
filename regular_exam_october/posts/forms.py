from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image_url', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Put an attractive and unique title...'}),
            'image_url': forms.URLInput(),
            'content': forms.Textarea(attrs={'placeholder': 'Share some '
                                                            'interesting facts about your adorable pets...'}),
        }
