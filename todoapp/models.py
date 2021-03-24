from django.db import models

# Create your models here.
class UserTodo(models.Model):
    uid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField(max_length=256)

    def __str__(self):
        return str(self.email)

class Todos(models.Model):
    tid=models.AutoField(primary_key=True)
    uid=models.ForeignKey(UserTodo,on_delete=models.CASCADE)
    title=models.CharField(max_length=30)
    description=models.CharField(max_length=200)
    status=models.CharField(max_length=10)
    data=models.DateField()

    def __str__(self):
        return str(self.title)

