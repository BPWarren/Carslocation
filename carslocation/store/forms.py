from django.forms import ModelForm, TextInput, EmailInput
from .models import Customer


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = {"name", "email", "address", "cni"}
        widgets = {
            "name": TextInput(
                attrs={
                    "class": "form-control form-control-sm",
                    "placeholder": "Full Name",
                }
            ),
            "email": EmailInput(
                attrs={"class": "form-control form-control-sm", "placeholder": "Email"}
            ),
            "cni": TextInput(
                attrs={"class": "form-control form-control-sm", "placeholder": "CNI"}
            ),
            "address": TextInput(
                attrs={
                    "class": "form-control form-control-sm",
                    "placeholder": "Address",
                }
            ),
        }
