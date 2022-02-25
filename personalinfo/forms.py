from django import forms
from .models import ContactProfile
from django.utils.translation import ugettext_lazy as _

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactProfile
        fields = ['name', 'title', 'email', 'message']
        labels = {
            'name': 'نام',
            'tite': 'عنوان',
            'email': 'ایمیل',
            'message': 'متن پیام'
        }
        widgets = {
            'name': forms.TextInput(attrs={
			'placeholder': _('*نام و نام خانوادگي ..'),
			'class': 'form-control'
			}),
			'title': forms.TextInput(attrs={
			'placeholder': _('*عنوان ..'),
			'class': 'form-control'
			}),
			'email': forms.EmailInput(attrs={
			'placeholder': _('*ايميل ...'),
			'class': 'form-control'
			}),
			'message': forms.Textarea(attrs={
			'placeholder': _('*پيام شما'),
			'class': 'form-control',
			'rows': 6,
			})
		}



	