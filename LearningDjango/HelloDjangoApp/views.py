from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    now = datetime.now()

    return render(
        request,
        "HelloDjangoApp/index.html",  # Relative path from the 'templates' folder to the template file
        # "index.html", # Use this code for VS 2017 15.7 and earlier
        {
            'content': "<strong>Hello Django!</strong> on " + now.strftime("%A, %d %B, %Y at %X"),
            'message': "Tiger Rules obvi lol",
            'content': " on " + now.strftime("%A, %d %B, %Y at %X")

        }
    )

def about(request):
    return render(
        request,
        "HelloDjangoApp/about.html",
        {
            'title' : "About HelloDjangoApp",
            'content' : "This is my sad little about page :("
        }
    )