from django.shortcuts import render, HttpResponse

# Create your views here.
def home(index):
	return HttpResponse("This is home")

def about(index):
	return HttpResponse("This is about")

def contact(index):
	return HttpResponse("This is contact")

