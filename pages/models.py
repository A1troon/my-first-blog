from django.conf import settings
from django.db import models
from django.forms import ModelForm
from django import forms



class Interest(models.Model):
    name = models.CharField(max_length=50)
    counter = models.IntegerField(default=0)
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
            return Interest.objects.create(name=xxx,counter=1)
        else:
            temp.counter += 1
            temp.save()
            return temp
    def isEmpty(x,y=None):
        for i in Interest.objects.all():
            if i.person_set.count()==0:
                i.delete()
    class Meta:
        ordering = ['-counter']

class Person(models.Model):
    name = models.CharField(max_length=128)
    group = models.CharField(max_length=20,default="нет группы")
    interests = models.ManyToManyField(Interest)
    def __str__(self):
        return self.name

#class student(models.Model):
#    name = models.ForeignKey(Person,on_delete=models.CASCADE)
#    interest = models.ForeignKey(Interest, on_delete=models.CASCADE)
#    group = models.CharField(max_length=20)
#    def __str__(self):
#        return self.group


#class studentForm(forms.Form):
#    name = forms.CharField( max_length=20)
#    group = forms.CharField(max_length=20)
#    interest = forms.CharField(max_length=50)



class UploadFileForm(forms.Form):
    file= forms.FileField()

