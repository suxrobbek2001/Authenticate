from django.contrib.auth.models import User
from django.db import models

class Student(models.Model):
    ism= models.CharField(max_length=30)
    yosh = models.PositiveSmallIntegerField()
    guruh = models.SmallIntegerField()
    foydalanuvchi = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f'{self.ism},{self.guruh}'
# Create your models here.
