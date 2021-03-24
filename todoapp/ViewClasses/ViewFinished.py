from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View
from django.contrib.auth.hashers import make_password,check_password
from todoapp.models import UserTodo,Todos
from django.http import HttpResponse,HttpResponseRedirect
import hashlib

# Create your views here.
class ViewFinished(View):
    def get(self,request):
        if "uid" in request.session:
            name=request.session.get('name',"none")
            uid=UserTodo.objects.filter(uid__exact=int(request.session.get("uid"))).get() 
            todos=Todos.objects.filter(uid__exact=uid,status="finish").order_by("-tid")
            user={
                "name":name,
                "todos":todos
            }
            return render(request,"finish.html",context=user)
        else:
            return redirect("login")

   
        


        

    


                




            


