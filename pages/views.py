import  requests
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse,HttpResponseNotFound
from .models import student, studentForm, Interest, Person, UploadFileForm
import requests
import io
def first(request):
    return render(request, 'pages/main.html', {})
def second(request):
    context={'interests': Interest.objects.all()}

    return render(request,"pages/favor.html",context)
def get_student(request):
    men = Person.objects.all()
    return render(request, "pages/chel.html", {"men": men})
def create(request):
    if request.method == "POST":
        new_person = Person.objects.create(name=request.POST.get("name"))
        new_interest = Interest.build(request.POST.get("interest"))
        new_student = student.objects.create(name=new_person, interest=new_interest, group=request.POST.get("group"))
        new_student.save()
    return HttpResponseRedirect("/123")

def Upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            a = request.FILES['file'].readline()
            while a:
                p=a.decode('utf-8').split(",")
                new_person = Person.objects.create(name=p[0])
                new_interest = Interest.build(p[2])
                new_student = student.objects.create(name=new_person, interest=new_interest, group=p[1])
                new_student.save()
                if len(p)>2:
                    i=3
                    while i<len(p):
                        new_interest = Interest.build(p[i])
                        new_student = student(name=new_person,interest=new_interest)
                        new_student.save()
                        i+=1
                a = request.FILES['file'].readline()
            return HttpResponse("гуд джоб")
    else:
            form=UploadFileForm()
    return render(request,'pages/download.html', {'form': form})

def clear_interest(request):
    Interest.objects.all().delete()
    return HttpResponse("очищено!")

def clear_student(request):
    student.objects.all().delete()
    Person.objects.all().delete()
    return HttpResponse("очищено!")



def delete(request, id):
    try:
        men = Person.objects.get(id=id)
        men.delete()
        Interest.isEmpty(123)
        return HttpResponseRedirect("/123")
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


def edit(request, id):
    try:
        men = Person.objects.get(id=id)

        if request.method == "POST":
            men.delete()
            Interest.isEmpty(123)
            new_person = Person.objects.create(name=request.POST.get("name"))
            new_interest = Interest.build(request.POST.get("interest"))
            new_student = student.objects.create(name=new_person, interest=new_interest,group=request.POST.get("group"))
            new_student.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "pages/edit.html", {"men": men})
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")
def add_more_interes(request, id):
    men = Person.objects.get(id=id)
    if request.method == "POST":
        new_interest = Interest.build(request.POST.get("interest"))
        new_student = student(name=men, interest=new_interest)
        new_student.save()

    return render(request,"pages/dopinteres.html",{})
def search(request):
    back = []
    mas=[]
    mas_string=[]
    for men in Person.objects.all():
       mas.append(men)
    if request.method == "POST":
        temp=0
        for i in range(Person.objects.all().count()-1):
            for j in range(i+1, Person.objects.all().count()):
                string=mas[i].name+" "+mas[j].name
                mas_string.append(string)
                for k in mas[i].interest_set.all():
                    for l in mas[j].interest_set.all():
                        if k.name==l.name:
                            temp+=1
                back.append(temp)
                temp=0
    return render(request,"pages/finally.html",{"persons":mas,"chisla":back,"chelovechki":mas_string})


#--------------------------------------------------------------------------------------------------
def vk(request):
    def first(id):
        token = '76270dc776270dc776270dc774765425087762776270dc7293e437330e1d750888753e4'
        version = '5.120'
        user_id = id
        response = requests.get('https://api.vk.com/method/users.getSubscriptions',
                                params={'access_token': token,
                                        'v': version,
                                        'user_id': user_id,

                                        }
                                )
        data = response.json()['response']['groups']['items']
        return data

    def second(id):
        token = '76270dc776270dc776270dc774765425087762776270dc7293e437330e1d750888753e4'
        version = '5.120'
        group_id = id
        secondresponse = requests.get('https://api.vk.com/method/groups.getById',
                                      params={'access_token': token,
                                              'v': version,
                                              'group_id': group_id
                                              }
                                      )
        seconddata = secondresponse.json()['response'][0]['name']
        return seconddata

    def third(id):
        token = '76270dc776270dc776270dc774765425087762776270dc7293e437330e1d750888753e4'
        version = '5.120'
        user_id = id
        response = requests.get('https://api.vk.com/method/users.get',
                                params={'access_token': token,
                                        'v': version,
                                        'user_id': user_id,
                                        'lang': 0,
                                        }
                                )
        data = response.json()['response'][0]['first_name']
        return data
    if request.method=='POST' :
        vkid=request.POST.get("vkid")
        myfile = io.open("media/hello.txt", "w", encoding="utf-8")
        name=third(vkid)
        myfile.write(name + ",")
        data=first(vkid)
        myfile.write("нет группы,")
        for i in data:
            myfile.write(second(i)+",")
        myfile.close()
        myfile = io.open("media/hello.txt", "r", encoding="utf-8")
        a = myfile.readline()
        p = a.split(",")
        new_person = Person.objects.create(name=p[0])
        new_interest = Interest.build(p[2])
        new_student = student.objects.create(name=new_person, interest=new_interest, group=p[1])
        new_student.save()
        if len(p) > 2:
            i = 3
            while i < len(p):
                new_interest = Interest.build(p[i])
                new_student = student(name=new_person, interest=new_interest)
                new_student.save()
                i += 1
        myfile.close()
        return HttpResponse("гуд джоб")
    return render(request,"pages/vk.html",{})
