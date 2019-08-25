from django import forms
from django.contrib.auth import authenticate
from core.models import *

class UserAuthenticateForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

    def clean(self):
        data = super().clean()
        user = authenticate(username=data['username'], password=data['password'])
        if user:
            data['user'] = user
            return data
        raise forms.ValidationError('Invalid login credentials!')

class FarmerRegistrationForm(forms.ModelForm):
    email = forms.EmailField()
    password = forms.CharField(max_length=100)

    class Meta:
        model = Expert
        fields=['user','name','phone','city','state','job']
    
    def save(self):
        user=User.objects.create(username=self.cleaned_data['email'], email=self.cleaned_data['email'])
        user.set_password(self.cleaned_data['password'])
        return super().save()