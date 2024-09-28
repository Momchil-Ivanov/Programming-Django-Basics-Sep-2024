from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    context = {
        "current_time": datetime.now(),
        "person": {
            "age": 20,
            "height": 190,
        },
        "ids": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "some_text": "Hello",
        "users": [
            "Pesho",
            "Ivan",
            "Stamat",
            "Maria",
            "Magdalena",
        ]
    }

    return render(request, 'base.html', context=context)

def dashboard(request):
    context = {
        "posts": [
            {
                "title": "How to create Django project?",
                "author": "Diyan Kalaydzhiev",
                "content": "I **really** don't <i>know</i> how to create a project",
                "created_at": datetime.now(),
            },
            {
                "title": "How to create Django project 1?",
                "author": "Diyan Kalaydzhiev",
                "content": "### I really don't know how to create a project",
                "created_at": datetime.now(),
            },
            {
                "title": "How to create Django project 2?",
                "author": "Diyan Kalaydzhiev",
                "content": "I really don't know how to create a project",
                "created_at": datetime.now(),
            },
        ]
    }

    return render(request, 'posts/dashboard.html', context=context)