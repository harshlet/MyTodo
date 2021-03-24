from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View
from django.contrib.auth.hashers import make_password,check_password
from todoapp.models import UserTodo,Todos
from django.http import HttpResponse,HttpResponseRedirect
import hashlib

# Create your views here.
class Finish(View):
    def get(self,request,tid):
        if "uid" in request.session:
            todo=Todos.objects.get(tid=tid)
            todo.status="finish"
            todo.save()
            return redirect("/")
        else:
            return redirect("login")

    
        


        

    


                




            


