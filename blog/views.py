from django.shortcuts import render, HttpResponse

# Create your views here.
def blogHome(request):
	return HttpResponse("We will keep all the blog post here.")


def blogPost(request, slug):
	return HttpResponse(f"This is blog post: {slug}")

