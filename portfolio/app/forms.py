from django import forms
from .models import contactModel

class contactFrom(forms.ModelForm):
      class Meta:
            model = contactModel
            fields = ['name', 'email', 'subject', 'message']
      def __init__(self, *args, **kwargs):
              super(contactFrom, self).__init__(*args, **kwargs)
              self.fields['name'].widget.attrs['class'] = 'form-control'
              self.fields['name'].widget.attrs['placeholder'] = 'Name*'
              self.fields['email'].widget.attrs['placeholder'] = 'Email*'
              self.fields['email'].widget.attrs['class'] = 'form-control'
              self.fields['subject'].widget.attrs['class'] = 'form-control'
              self.fields['message'].widget.attrs['class'] = 'form-control'   
              self.fields['subject'].widget.attrs['placeholder'] = 'Subject'
              self.fields['message'].widget.attrs['placeholder'] = 'Message*'
              