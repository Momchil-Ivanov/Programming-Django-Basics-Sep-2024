from django import forms
from .models import Author


class AuthorProfileForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'passcode', 'pets_number']

        widgets = {
            'passcode': forms.PasswordInput(attrs={
                'placeholder': 'Enter 6 digits...',
                'maxlength': '6'
            }),
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Enter your first name...',
                'maxlength': '40'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Enter your last name...',
                'maxlength': '50'
            }),
            'pets_number': forms.NumberInput(attrs={
                'placeholder': 'Enter the number of your pets...',
                'min': '0'
            }),
        }

    def clean_passcode(self):
        passcode = self.cleaned_data.get('passcode')
        if len(passcode) != 6 or not passcode.isdigit():
            raise forms.ValidationError("Passcode must be a combination of 6 digits.")
        return passcode


class AuthorEditForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'pets_number', 'info', 'image_url']

        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Enter your first name...',
                'maxlength': '40'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Enter your last name...',
                'maxlength': '50'
            }),
            'pets_number': forms.NumberInput(attrs={
                'placeholder': 'Enter the number of your pets...',
                'min': '0'
            }),
            'info': forms.Textarea(attrs={
                'placeholder': 'Enter some information about yourself...',
                'cols': 40,
                'rows': 10,
            }),
            'image_url': forms.URLInput(attrs={
                'placeholder': 'Enter your profile image URL...',
                'maxlength': '200'
            }),
        }

    def clean_passcode(self):
        return self.cleaned_data.get('passcode')
