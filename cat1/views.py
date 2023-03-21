from django.shortcuts import render

def home(request):
    return render(request,'about.html')

def blog(request):
    return render(request,'blog.html')

def cliet(request):
    return render(request,'client.html')

def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def service(request):
    return render(request,'services.html')
