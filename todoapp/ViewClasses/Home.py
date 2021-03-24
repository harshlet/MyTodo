from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View
from django.contrib.auth.hashers import make_password,check_password
from todoapp.models import UserTodo,Todos
from django.http import HttpResponse,HttpResponseRedirect
import hashlib
import datetime

# Create your views here.
class Home(View):
    def get(self,request):
        if "uid" in request.session:
            name=request.session.get('name',"none")
            uid=UserTodo.objects.filter(uid__exact=int(request.session.get("uid"))).get() 
            todos=Todos.objects.filter(uid__exact=uid,status="pending").order_by("-tid")
            user={
                "name":name,
                "todos":todos
            }
            return render(request,"home.html",context=user)
        else:
            return redirect("todo:login")

    def post(self,request):
        title=request.POST.get("title")
        description=request.POST.get("description")
        status="pending"
        uid=UserTodo.objects.filter(uid__exact=int(request.session.get("uid"))).get() 
        todo=Todos(uid=uid,title=title,description=description,status=status,data=datetime.date.today())
        todo.save()
        respnce=HttpResponseRedirect("/")
        return respnce
        


        

    


                




            


