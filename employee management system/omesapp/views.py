from django.shortcuts import render,redirect
from omesapp.models import Employee
from omesapp.forms import Employee_form
from django.http import HttpResponse
# Create your views here.
def Index(request):
    return render(request,'omesapp/index.html')


def All_view(request):
    data = Employee.objects.all()
    return render(request,'omesapp/all.html',{'data':data})


def Add_view(request):
    form = Employee_form()
    if request.method == "POST":
        form=Employee_form(request.POST)
        if form.is_valid():
            form.save()
            #return HttpResponse("Employee details added successfully")
       
            return redirect('/index')
           
    return render(request,'omesapp/add.html',{'form':form})


def Delete_view(request):
    data = Employee.objects.all()
    return render(request,'omesapp/delete.html',{'data':data})

def Delete(request,id):
    data = Employee.objects.get(id=id)
    data.delete()
    return redirect("/del")

def Update_view(request):
    data = Employee.objects.all()
    return render(request,'omesapp/update.html',{'data':data})

def Update(request,id):
    data = Employee.objects.get(id=id)
    form = Employee_form(instance=data)

    if request.method=="POST":
        form =Employee_form(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect("/index")
    return render(request,'omesapp/update.html',{'form':form})


def Filter(request):
    data = Employee.objects.filter(salary__gt=50000)
    return render(request,'omesapp/filter.html',{'data':data})



