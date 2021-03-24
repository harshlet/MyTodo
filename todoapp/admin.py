from django.contrib import admin
from .models import Todos,UserTodo

# Register your models here.
admin.site.register(Todos)
admin.site.register(UserTodo)
