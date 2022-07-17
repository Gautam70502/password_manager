from ast import Pass
import email
from email.mime import application
from multiprocessing import context
from django.shortcuts import redirect, render
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from Main_app import models
from Main_app.forms import Appform

from Main_app.models import Password_Manager

# Create your views here.


def login(request):

    context ={}
    if request.method == 'POST':
        usernname = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(usernname = usernname,password=password)
        request.session['username'] = usernname
       

        if user is not None:
            auth.login(request,user)
            print("user is login")
            redirect("index/")
       

    else:    
     return render(request,"Login.html")


def register(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['confirm_password']
        name = request.POST['name']
        email = request.POST['email']
        if(password == password1):
           
                user = User.objects.create_user(username = username,password = password,first_name = name,email=email)
               
                user.save();  
                print("user created")
                return redirect('/')
                 
        else:
            print("incorrect password")

    else:

     return render(request,"Register.html")    


def index(request):

     
     return render(request,"index.html",)


def addapp(request):

    context ={}
    if request.method == 'POST':
        logo = request.POST['logo']
        application_name = request.POST['app_name']
        email = request.POST['email']
        password = request.POST['password']
        

      
        context["dataset"] = Password_Manager.objects.all()
        obj = Password_Manager.objects.create(logo = logo,Email = email,password=password,application_name = application_name)
        obj.save()
        return render(request,"index.html",context)
       






    else:

     return render(request,"Add_App.html",context)


#def delete(request,pk):

    delete_app = Password_Manager.objects.get(id = pk)
    delete_app.delete()
    return redirect("/index")


#def update(request,pk):  
    application = Password_Manager.objects.get(id =pk)  
    form = Appform(request.POST, instance = application)  
    if form.is_valid():  
        form.save()  
        
    return render(request, 'Add_App.html', {'application': application})  


