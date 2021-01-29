from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def create(request):
    return HttpResponse("Página de create")

def list(request):
    return HttpResponse("Página de list")

def update(request):
    return HttpResponse("Página de update")


