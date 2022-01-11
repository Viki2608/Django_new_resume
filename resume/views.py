from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Projects

# Create your views here.

def index(request):
    project1=Projects()
    project1.name= "Simple Web Resume "
    project1.desc="Created Resume using HTML,CSS,JS,Bootstrap and deployed in github pages"
    project2=Projects()
    project2.name= "Virtual Voice Assistant "
    project2.desc="Voice recognition Virtual assistant using Python"
    project3=Projects()
    project3.name= "Pong Game"
    project3.desc="Vintage Pong game using Python Turtle module and Tkinter"
    project4=Projects()

    project4.name= "Infix Prefix Postfix Converter"
    project4.desc="A simple Desktop Application to convert infix postfix prefix expression Using Python Tkinter."

    project5=Projects()

    project5.name= "Weather app"
    project5.desc="Created using HTML ,Node js , Express ,Open weather api"
    project6=Projects()

    project6.name= "Password Manager"
    project6.desc="Created a password manager with tkinter interface ,Postgres,Python"
    project=[project1,project2,project3,project4,project5,project6]
    

    return render(request,'index.html',{'projects': project })
