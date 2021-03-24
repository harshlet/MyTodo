
from django.contrib import admin
from django.urls import path
from . import views

app_name="todo"
urlpatterns = [
    path('login', views.Login.as_view(),name="login"),
    path('', views.Home.as_view(),name="home"),
    path('logout', views.logout,name="logout"),
    path('finishedwork', views.ViewFinished.as_view(),name="workfinish"),
    path('finish/<int:tid>', views.Finish.as_view(),name="finish"),
]
