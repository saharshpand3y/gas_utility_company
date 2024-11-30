from django import forms
from .models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True, label="Your Name")
    email = forms.EmailField(required=True, label="Your Email")
    phone = forms.CharField(max_length=15, required=True, label="Your Phone")
    address = forms.CharField(widget=forms.Textarea, required=True, label="Your Address")

    class Meta:
        model = ServiceRequest
        fields = ['request_type', 'details', 'attachment']
