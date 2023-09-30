from django.shortcuts import render

# Create your views here.

def renderIndex(request):
    return render(request,'templatesApp\index.html')