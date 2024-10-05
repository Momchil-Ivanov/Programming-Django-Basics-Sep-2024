from crispy_forms.helper import FormHelper
from django import forms
from django.core.exceptions import ValidationError
from django.forms import formset_factory

from forumApp.posts.choices import LanguageChoice
from forumApp.posts.mixins import DisableFieldMixin
from forumApp.posts.models import Post, Comment


class PostBaseForm(forms.ModelForm):
    extra_description = forms.CharField()

    class Meta:
        model = Post
        fields = "__all__"

        error_messages = {
            'title': {
                'required': 'Please write something',
                'max_length': f'Title is too long. Please keep it under {Post.TITLE_MAX_LENGTH} characters.',
            },
            'author': {
                'required': 'Please enter an author',
            },
        }

    def clean_author(self):
        author = self.cleaned_data.get('author')

        if author[0].islower():
            raise ValidationError('Author name must start with an uppercase letter!')

        return author

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')

        if title and content and title in content:
            raise ValidationError('Title must not be in content!')

        return cleaned_data

    def save(self, commit=True):
        post = super().save(commit=False)

        post.title = post.title.capitalize()

        if commit:
            post.save()

        return post


class PostCreateForm(PostBaseForm):
    pass


class PostEditForm(PostBaseForm):
    pass


class PostDeleteForm(PostBaseForm, DisableFieldMixin):
    disabled_fields = ('title', 'content')
    pass


class SearchForm(forms.Form):
    query = forms.CharField(
        label='',
        required=False,
        error_messages={
            'required': 'Please write something',
        },
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search for a post...',
            }
        )
    )

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #
    #     self.helper = FormHelper()
    #     self.helper.form_method = 'get'
    #     self.helper.form_class = 'form-inline'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'content',)

        labels = {
            'author': '',
            'content': '',
        }

        error_messages = {
            'author': {
                'required': 'Author name is required. Write it!',
            },
            'content': {
                'required': 'Content is required. Write it!',
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['author'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Your name'
        })

        self.fields['content'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Your comment',
            'rows': 1,
        })


CommentFormSet = formset_factory(CommentForm, extra=1)