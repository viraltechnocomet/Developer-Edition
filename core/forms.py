from django import forms
from django.forms import ModelForm
from . import models
from django.contrib.auth import get_user_model
from django.contrib.admin import widgets
from accounts.models import *
from core.models import *



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
                    'placeholder':"User Name",
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
            'password':forms.PasswordInput(
                attrs={
                    'required' : True,
                    'class':'form-control',
                    'placeholder':"Password",
                    'type':"text",
                }
            ),
            
       }     

     
class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=['category_name']     


class PolicyForm(forms.ModelForm):
    # username = forms.CharField(, to_field_name="id")
    category=forms.ModelChoiceField(queryset=Category.objects.all(),empty_label="Category Name", to_field_name="id")
    class Meta:
        model=Policy
        fields=['email','policy_name','sum_assurance','premium','tenure']


