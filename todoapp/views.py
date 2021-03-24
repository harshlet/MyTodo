from django.shortcuts import render,redirect
from .ViewClasses.Login import Login
from .ViewClasses.Home import Home
from .ViewClasses.Finish import Finish
from .ViewClasses.ViewFinished import ViewFinished

# Create your views here.
def logout(request):
    if "uid" in request.session:
        del request.session['uid']
        del request.session['email']
        del request.session['name']
        return redirect("/")
    else:
        return redirect("/")
