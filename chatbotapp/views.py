from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def login(request):
    return render(request,'login.html')
def register(request):
    return render(request,'register.html')
def chatbot(request):
    return render(request,'chatbot.html')

