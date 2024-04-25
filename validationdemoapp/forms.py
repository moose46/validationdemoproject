from django import forms

from validationdemoapp.models import UserRegistration


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserRegistration
        fields = "__all__"
