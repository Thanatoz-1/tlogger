from django.shortcuts import render

def index(request):
	return render(request, 'blog/bmain.html')
	

# Create your views here.
