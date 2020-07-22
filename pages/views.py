from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse,HttpResponseNotFound
from .models import student, studentForm, Interest, Person, UploadFileForm
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
                p=a.split()
                new_person = Person.objects.create(name=p[0].decode('utf-8'))
                new_interest = Interest.build(p[2].decode('utf-8'))
                new_student = student.objects.create(name=new_person, interest=new_interest, group=p[1].decode('utf-8'))
                new_student.save()
                if len(p)>2:
                    i=3
                    while i<len(p):
                        new_interest = Interest.build(p[i].decode('utf-8'))
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