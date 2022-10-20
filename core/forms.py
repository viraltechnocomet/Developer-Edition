from django import forms
from django.forms import ModelForm

from accounts.models import CustomUser

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
                    'placeholder':"username",
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
        
class AddAgentForm(ModelForm):
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
                    'placeholder':"username",
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
                    'type':"password",
                }
            ),
            
        }

# class AccountManagerForm(forms.ModelForm):

#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email', 'profile_image', )

#     def clean_email(self):
#         email = self.cleaned_data['email'].lower()
#         try:
#             account = CustomUser.objects.exclude(pk=self.instance.pk).get(email=email)
#         except CustomUser.DoesNotExist:
#             return email
#         raise forms.ValidationError('Email "%s" is already in use.' % account)

#     def clean_username(self):
#         username = self.cleaned_data['username']
#         try:
#             account = CustomUser.objects.exclude(pk=self.instance.pk).get(username=username)
#         except CustomUser.DoesNotExist:
#             return username
#         raise forms.ValidationError('Username "%s" is already in use.' % username)


#     def save(self, commit=True):
#         account = super(AccountManagerForm, self).save(commit=False)
#         account.username = self.cleaned_data['username']
#         account.email = self.cleaned_data['email'].lower()
#         account.profile_image = self.cleaned_data['profile_image']
#         if commit:
#             account.save()
#         return account
    
    
        


