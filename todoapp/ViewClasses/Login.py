from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View
from django.contrib.auth.hashers import make_password,check_password
from todoapp.models import UserTodo
from django.http import HttpResponse
import hashlib

# Create your views here.
class Login(View):
    def get(self,request):
        return render(request,"login.html")

    def post(self,request):
        form = request.POST.get('form')
        if form=="signup":
            name=request.POST.get('name')
            email=request.POST.get('email')
            usercheck=UserTodo.objects.filter(email__exact=email)
            if usercheck:
                return render(request,"login.html",context={"emailexist":True})
            password=request.POST.get('password')
            hpass = hashlib.sha256(str(password).encode()).hexdigest()
            
            user=UserTodo()
            user.name=name
            user.email=email
            user.password=hpass
            user.save()
            return render(request,"login.html",context={"register":True})
        elif form=="login":
            email=request.POST.get('email')
            password=request.POST.get('password')
            
            hpass =  hashlib.sha256(str(password).encode()).hexdigest()
            
            user=UserTodo.objects.filter(email__exact=email,password__exact=hpass)
            
            if user:
                    result=user.get()
                    request.session['uid']=result.uid
                    request.session['email']=result.email
                    request.session['name']=result.name
                    return redirect("/")
            else:
                return render(request,"login.html",context={"wrong":True})


                




            


