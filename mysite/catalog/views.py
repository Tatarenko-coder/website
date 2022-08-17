from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def project(request):
    return render(request, "project1.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")
