from .models import *
from django import forms
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['business_title', 'business_address', 'business_email', 'business_phone', 'business_gst']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255,label='username')
    password = forms.CharField(widget=forms.PasswordInput,label='password')

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')
    
    # Corrected business fields
    business_title = forms.CharField(max_length=100, required=False, label='Business Title')
    business_address = forms.CharField(max_length=400, required=False, widget=forms.Textarea, label='Business Address')
    business_email = forms.EmailField(required=False, label='Business Email')
    business_phone = forms.CharField(max_length=20, required=False, label='Business Phone')
    business_gst = forms.CharField(max_length=15, required=False, label='Business GST')

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password', 'business_title', 'business_address', 'business_email', 'business_phone', 'business_gst']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data

class BillingForm(forms.ModelForm):
    class Meta:
        model=Billing
        fields = ['bill_id','bill_date']
        widgets={
            'bill_date':forms.DateInput(attrs={
                                'type':'date'

            })
        }
        
    

class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['customer_name','customer_address','customer_mobileno','customer_gst']