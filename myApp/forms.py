from django import forms
from django.forms import TextInput, EmailInput, URLInput, Textarea

from .models import Company, Applicant


class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone",
            "linkedin_profile",
            "personal_website",
            "personal_note",
            # "resume"
        ]
        widgets = {
            ("first_name", "last_name", "phone"): TextInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 400px;",
                    "placeholder": "Enter Text",
                }
            ),
            "email": EmailInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 400px;",
                    "placeholder": "Email",
                }
            ),
            ("linkedin_profile", "personal_website"): URLInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 400px;",
                    "placeholder": "URL",
                }
            ),
            "personal_note": Textarea(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 400px;",
                    "placeholder": "Note",
                }
            ),
        }


# class ApplicantForm2(forms.Form):  # Candidate
#     # company = forms.ForeignKey(Company, on_delete=models.CASCADE)  # del
#     first_name = forms.CharField(label="first-name", max_length=50)  # , blank=False
#     last_name = forms.CharField(label="last-name", max_length=50)  # , blank=False
#     email = forms.EmailField(label="your-mail")  # blank=False
#     phone = forms.CharField(label="your-phone")  # max_length=10
#     linkedin_profile = forms.URLField(label="linkedin-profile")  # linkedin_url
#     personal_website = forms.URLField(label="your-site")
#     personal_note = forms.CharField(label="note", widget=forms.Textarea)

    # resume = forms.FileField()  # blank=False
    # cover_letter = forms.FileField()
    # portfolio

    # class Meta:
    #     model = Company
