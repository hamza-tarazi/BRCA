from django import forms
from django.contrib.auth.forms import UserCreationForm
from core.models import User
from .models import Customer

class UserRegisterForm(UserCreationForm):
    username= forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Name"}))
    email= forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"Email"}))
    subject= forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Subject"}))
    message= forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Message"}))
    class Meta:
        model = User
        fields=['username', 'email', 'subject', 'message']
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['username', 'email', 'telephone', 'subject', 'message']
        widgets = {
            'username': forms.TextInput(attrs={"placeholder": "Name"}),
            'email': forms.EmailInput(attrs={"placeholder": "Email"}),
            'telephone': forms.TextInput(attrs={"placeholder": "Telephone"}),
            'subject': forms.TextInput(attrs={"placeholder": "Subject"}),
            'message': forms.Textarea(attrs={"placeholder": "Message"}),
        }
    