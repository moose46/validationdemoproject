import re

from django import forms
from django.forms import (
    DateInput,
    EmailInput,
    PasswordInput,
    RadioSelect,
    Select,
    URLInput,
)

from validationdemoapp.models import UserRegistration


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserRegistration
        fields = "__all__"
        genders = [("male", "Male"), ("female", "Female")]
        countries = [
            ("select", "Please Choose Country"),
            ("India", "India"),
            ("Australia", "Australia"),
            ("America", "America"),
            ("Spain", "Spain"),
        ]

        widgets = {
            "password": PasswordInput(),
            "confirm_password": PasswordInput(),
            "gender": RadioSelect(choices=genders),
            "country": Select(choices=countries),
            "date_of_birth": DateInput(attrs={"type": "date"}),
            "email": EmailInput(),
            "website_url": URLInput(),
        }

    # Field level validations
    def clean_phone_number(self):
        if iphonenumber := self.cleaned_data.get("phone_number"):
            # pattern = re.compile(f"(0|91)?[6-9][0-9]{9}")
            pattern = re.compile("^(([0-9]{3}) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$")
            if not re.fullmatch(pattern, iphonenumber):
                raise forms.ValidationError(
                    "Invalid Phone Number! Example: +911234567891"
                )
            return iphonenumber

    def clean(self):
        cleaned_data = super().clean()
        ipassword = cleaned_data.get("password")
        iconfirm_password = cleaned_data.get("confirm_password")
        if ipassword and iconfirm_password and ipassword != iconfirm_password:
            raise forms.ValidationError("Passwords do not match.")

        iusername = cleaned_data.get("username")
        if ipassword and iusername and ipassword == iusername:
            raise forms.ValidationError(
                "User Name and password should not be the same..."
            )

        country = cleaned_data.get("country")
        if country == "select":
            raise forms.ValidationError("Please Choose a Country.")

        if not cleaned_data.get("terms_conditions"):
            raise forms.ValidationError("Please agree to terms and condidtions")

        return cleaned_data
