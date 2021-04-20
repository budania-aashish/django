from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(*args, **kwargs):
    return HttpResponse("<h1>Home!</h1>")


def contact_view(*args, **kwargs):
    return HttpResponse("<h1>Contact!</h1>")


def about_view(*args, **kwargs):
    return HttpResponse("<h1>About!</h1>")
