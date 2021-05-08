from django.shortcuts import render, HttpResponse
from django.contrib import messages
from home.models import Contact
from blog.models import Post

def home(request):
	allPosts = Post.objects.all()
	context = {'allPosts': allPosts}
	return render(request, 'home/home.html',context)

def about(request):
	return render(request, 'home/about.html')

def contact(request):
	if request.method == "POST":
		name = request.POST.get('name','')
		email = request.POST.get('email','')
		phone =  request.POST.get('phone','')
		content = request.POST.get('content','')
		if len(name) < 2 or len(email)<3 or len(phone)<10 or len(content)<4:
			messages.error(request, "Please fill the form correctly!")
		else:
			contact = Contact(name=name, email=email, phone=phone, content=content)
			contact.save()
			messages.success(request, "Your message has been sent!")
	return render(request, 'home/contact.html')