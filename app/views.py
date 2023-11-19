from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request,'hello/index.html')

def home (request):
    return render(request,'home/home.html')