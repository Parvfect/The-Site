from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import User, StoryCategory, Story, Imp, ReadingList, Studio


def start(request):
    return render(request, 'homepage.html')
        

def home(request):
    return render(
        request = request,
        template_name = "homepage.html")



def rl(request):
    return render(request, "readinglist.html", context = {"books":ReadingList.objects.all})

def writings(request):
    return render(
        request,
         "writings.html",
         context = {"categories":StoryCategory.objects.all}
         )

def stories(request):
    t = Story.objects.filter(category = 1)
    return render(
        request,
         "stories.html",
         context = {"stories":t}
         )

def StoryContent(request, story_name):
    name = Story.objects.filter(slug = story_name)
    count = name.count()
    context ={
        "obj":name,
    }
    return render(
        request,
        "template.html",
        context = context
    )

def BookSummary(request, book_name):
    name = ReadingList.objects.filter(name = book_name)
    context = {
        "obj":name
    }
    return render (
        request,
        "bookreview.html",
        context
    )

def essays(request):
    t = Story.objects.filter(category = 2)
    return render(
        request,
         "essays.html",
         context = {"stories":t}
         )

def funl(request):
    t = Story.objects.filter(category = 3)
    return render(
        request,
         "funliners.html",
         context = {"stories":t}
         )


def imp(request):
    return render(
        request, 
        "imp.html",
        context = {"imp":Imp.objects.all}
        )

def books(request):
    return render(request, "books.html")

def bio(request):
    return render(request, "details.html")

def studio(request):
    return render(request, "studio.html", context = {"content":Studio.objects.all})