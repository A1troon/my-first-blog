from django.conf import settings
from django.db import models
from django.forms import ModelForm
from django import forms

class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Interest(models.Model):
    name = models.CharField(max_length=50)
    students = models.ManyToManyField(Person, through='student')
    def __str__(self):
        return self.name
    def isExist(poisk):
        for i in Interest.objects.all():
            if i.name==poisk:
                return i
        return None
    def build(xxx):
        temp=Interest.isExist(xxx)
        if temp==None:
            return Interest.objects.create(name=xxx)
        else:
            return temp
    def isEmpty(x,y=None):
        for i in Interest.objects.all():
            if i.students.count()==0:
                i.delete()



class student(models.Model):
    name = models.ForeignKey(Person,on_delete=models.CASCADE)
    interest = models.ForeignKey(Interest, on_delete=models.CASCADE)
    group = models.CharField(max_length=20)
    def __str__(self):
        return self.group


class studentForm(forms.Form):
    name = forms.CharField( max_length=20)
    group = forms.CharField(max_length=20)
    interest = forms.CharField(max_length=50)



class UploadFileForm(forms.Form):
    file= forms.FileField()

