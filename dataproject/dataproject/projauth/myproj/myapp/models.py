from django.db import models
from django.contrib import admin
# Create your models here.
class Student(models.Model):
    refno=models.CharField(max_length=6,primary_key=True)
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    mail=models.EmailField()


class lab(models.Model):
    class Meta():
        permissions=[
            ("view_labs","can view lab details")
        ]
    labname=models.CharField( max_length=100)
    labbudget=models.IntegerField()


class StudentAdmin(admin.ModelAdmin):
    list_display=('refno','name','age','mail')


class labAdmin(admin.ModelAdmin):
    list_display=('labname','labbudget')