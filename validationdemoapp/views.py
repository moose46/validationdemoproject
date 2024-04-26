from django.shortcuts import render

from validationdemoapp.forms import UserRegistrationForm


# Create your views here.
def SignUp(request):
    form = UserRegistrationForm()
    template = "validationdemoapp/SignUp.html"
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # form.save()
            return render(request, "validationdemoapp/Home.html")
    else:
        form = UserRegistrationForm()

    return render(request, template, {"form": form})
