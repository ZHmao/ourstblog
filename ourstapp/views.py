from django.shortcuts import render_to_response
from django.http import HttpResponse

# Create your views here.

def homepage1(req):
    return HttpResponse('what')

def homepage(req):
    return render_to_response('index.html')

def contact(req):
	return render_to_response('contact.html')

def about(req):
	return render_to_response('about.html')

def post(req):
	return render_to_response('post.html')
