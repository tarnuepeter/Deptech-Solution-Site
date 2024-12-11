from django import forms
from .models import Post, Inquery, Booking
from ckeditor.fields import RichTextFormField


class ImageForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("header_image",)
        labels = {
            "header_image": "",
        }


class InqueryForm(forms.ModelForm):
    class Meta:
        model = Inquery
        fields = ("name", "email", "contact", "subject", "message")

        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Your Name"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Your Email"}
            ),
            "contact": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Active Contact Number"}
            ),
            "subject": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Subject"}
            ),
            "message": RichTextFormField(),
        }


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ("name", "address", "business", "contact", "email", "service")

        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Your Name"}
            ),
            "address": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Your Address"}
            ),
            "business": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Your business Name",
                }
            ),
            "contact": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Active Contact Number"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Your Email"}
            ),
            "service": forms.Select(attrs={"class": "form-control"}),
        }
