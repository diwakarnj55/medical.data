from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def html(request):
    return render(request,"404.html")
def appointment(request):
    return render(request,"appointment.html")
def contact(request):
    return render(request,"contact.html")
def feature(request):
    return render(request,"feature.html")
def service(request):
    return render(request,"service.html")
def testimonial(request):
    return render(request,"testimonial.html")
def team(request):
    return render(request,"team.html")

