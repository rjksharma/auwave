from django.shortcuts import render, redirect
from .models import *

# Create your views here.


def home(request):
    auwavedetails = AuwaveDetails.objects.all()
    services = Services.objects.all()
    data = {
        "title": "auwave | Home",
        "auwavedetails": auwavedetails,
        "services": services,
    }
    return render(request, "index.html", {"data": data})


def about(request):
    auwavedetails = AuwaveDetails.objects.all()
    ourteams = OurTeams.objects.all()
    data = {
        "title": "auwave | About",
        "ourteams": ourteams,
        "auwavedetails": auwavedetails,
    }
    return render(request, "about.html", {"data": data})


def services(request):
    services = Services.objects.all()
    auwavedetails = AuwaveDetails.objects.all()
    data = {
        "title": "auwave | Services",
        "services": services,
        "auwavedetails": auwavedetails,
    }
    return render(request, "services.html", {"data": data})


def portfolio(request):
    services = Services.objects.all()
    auwavedetails = AuwaveDetails.objects.all()
    data = {
        "title": "auwave | Services",
        "services": services,
        "auwavedetails": auwavedetails,
    }
    return render(request, "portfolio.html", {"data": data})


def contact(request):
    auwavedetails = AuwaveDetails.objects.all()
    data = {"title": "auwave | Contact", "auwavedetails": auwavedetails}
    return render(request, "contact.html", {"data": data})


def get_quote(request):
    auwavedetails = AuwaveDetails.objects.all()
    data = {"title": "auwave | Get a Quote", "auwavedetails": auwavedetails}
    return render(request, "get_quote.html", {"data": data})


def read_more(request, id):
    services = Services.objects.filter(id=id)
    auwavedetails = AuwaveDetails.objects.all()
    data = {
        "title": "auwave | Home",
        "auwavedetails": auwavedetails,
        "services": services,
    }
    return render(request, "read_more.html", {"data": data})


def user_contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        number = request.POST["number"]
        subject = request.POST["subject"]
        message = request.POST["message"]
        user_contact = UserConnect.objects.create(
            name=name,
            email=email,
            number=number,
            subject=subject,
            message=message,
        )
        return render(request, "successful.html")

    else:
        return render(request, "index.html")
