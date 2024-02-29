from django.shortcuts import render
from .models import Doubts


def index(request):
    # template = loader.get_template('home.html')
    # return HttpResponse(template.render())
    return render(request, 'home.html')


def home(request):
    return render(request, 'home.html')
    # return HttpResponse("This is homepage")


def about(request):
    return render(request, 'about.html')

    # return HttpResponse("This is aboupage")


def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        akshay = Doubts(name=name, email=email, phone=phone, desc=desc)
        akshay.save()

    return render(request, 'contacts.html')


def cmdept(request):
    return render(request, 'cmdept.html')


def mbdept(request):
    return render(request, 'mbdept.html')


def adept(request):
    return render(request, 'adept.html')
