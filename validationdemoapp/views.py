from django.shortcuts import render

from validationdemoapp.forms import UserRegistrationForm


# Create your views here.
def SignUp(request):
    form = UserRegistrationForm()
    template = "validationdemoapp/SignUp.html"
    return render(request, template, {"form": form})
