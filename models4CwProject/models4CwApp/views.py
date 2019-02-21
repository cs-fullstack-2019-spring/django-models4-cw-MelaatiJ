from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Child
from .models import Mom

#my functions


def index():

    return


def children():
    return None


def moms():
    return None


def addChild():
    return None


def deleteMom():
    print (Mom.objects.all())
    dm =
    dm.delete()
    print( print(Mom.objects.all()))