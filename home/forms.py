from django import forms
from .models import Contact
from django.core.exceptions import ValidationError
import re


# model form
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone']
        # widgets = {
        #     'name': forms.TextInput(attrs={
        #         'placeholder': 'Enter Your Name',
        #         'class': 'form-input',
        #     }),
        #     'phone': forms.TextInput(attrs={
        #         'placeholder': 'Enter Your Phone Numberrrr',
        #         'pattern': r'^\+?[0-9\s\-()]*$',
        #      }),
        # }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not re.match(r'^\+?[0-9\s\-()]*$', phone):
            raise ValidationError('Invalid phone number format.')
        return phone


#regular form
# class ContactForm(forms.Form):
#     name = forms.CharField(
#         max_length=100,
#         required=True,
#         widget=forms.TextInput(attrs={
#             'placeholder': 'Enter Your Name',
#             'class': 'form-input'
#         })
#     )
#     phone = forms.CharField(
#         max_length=15,
#         required=True,
#         widget=forms.TextInput(attrs={
#             'placeholder': 'Enter Your Phone Number',
#             'class': 'form-input',
#             'pattern': r'(\+?\d{1,4}[\s\-]?)?(\(?\d{1,4}\)?[\s\-]?)?\d{1,4}[\s\-]?\d{1,4}[\s\-]?\d{1,4}',
#         })
#     )
