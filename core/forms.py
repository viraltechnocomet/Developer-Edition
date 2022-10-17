from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.admin import widgets

User = get_user_model()

class CreateUserCustomForm(ModelForm):
    class Meta:
        model = User

        fields = "__all__"

        widgets = {
            'type':forms.HiddenInput(),
            'username':forms.TextInput(
                attrs={
                    'required' : True,
                    'class':'form-control',
                    'placeholder':"UserName",
                    'type':"text",
                }
            ),
            'email':forms.TextInput(
                attrs={
                    'required' : True,
                    'class':'form-control',
                    'placeholder':"E-Mail",
                    'type':"text",
                }
            ),
            'password1':forms.PasswordInput(
                attrs={
                    'required' : True,
                    'class':'form-control',
                    'placeholder':"Password",
                    'type':"text",
                }
            ),
            'password2':forms.PasswordInput(
                attrs={
                    'required' : True,
                    'class':'form-control',
                    'placeholder':"Confirm Password",
                    'type':"text",
                }
            ),
        }
               
class AddManagerForm(ModelForm):
    class Meta:
        model = User

        fields = "__all__"

        widgets = {
            'type':forms.HiddenInput(),
            
            'first_name':forms.TextInput(
                attrs={
                    'required' : True,
                    'class':'form-control',
                    'placeholder':"First Name",
                    'type':"text",
                }
            ),
            'last_name':forms.TextInput(
                attrs={
                    'required' : True,
                    'class':'form-control',
                    'placeholder':"Last Name",
                    'type':"text",
                }
            ),
            'username':forms.TextInput(
                attrs={
                    'required' : True,
                    'class':'form-control',
                    'placeholder':"User Name",
                    'type':"text",
                }
            ),
            'email':forms.EmailInput(
                attrs={
                    'required' : True,
                    'class':'form-control',
                    'placeholder':"E-Mail",
                    'type':"text",
                }
            ),
            'password':forms.PasswordInput(
                attrs={
                    'required' : True,
                    'class':'form-control',
                    'placeholder':"Password",
                    'type':"text",
                }
            ),
            
        }

        def save(self, commit=True):
            User = super(AddManagerForm, self).save(commit=False)
            User.username = self.cleaned_data['username']
            User.first_name = self.cleaned_data['first_name']
            User.last_name = self.cleaned_data['last_name']
            User.email = self.cleaned_data['email'].lower()
            User.profile_image = self.cleaned_data['profile_image']
            if commit:
                User.save()
            return User


# class ManagerForm(ModelForm):
#     class Meta:
        


