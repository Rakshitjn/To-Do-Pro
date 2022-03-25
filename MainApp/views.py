from django.http import request
from django.shortcuts import redirect, render
from .models import ToDoList
# Create your views here.
def index(request):
    data1 = ToDoList.objects.filter(status = 1)
    data2 = ToDoList.objects.filter(status = 0)
    param = {'data':data1 , 'data0':data2}
    return render(request, 'MainApp/todolis.html',param)

def done(request,pk):
    if request.method == 'POST':
        if (request.POST.get('stat')) == 'on':
            data = ToDoList.objects.get(id = pk)
            data.status = 0
            data.save()
            return redirect('main:index')
        else:
            return redirect('main:index')
    
    data = ToDoList.objects.get(id = pk)
    param = {'details':data, 'status':'Done !', 'ask': 'not done?'}
    return render(request,'MainApp/desc.html',param)


def notdone(request,pk):
    if request.method == 'POST':
        if (request.POST.get('stat')) == 'on':
            data = ToDoList.objects.get(id = pk)
            data.status = 1
            data.save()
            return redirect('main:index')
        else:
            return redirect('main:index')
    data = (ToDoList.objects.get(id = pk))
    param = {'details': data, 'status':"Not Done!", 'ask':'done?'}
    return render(request,'MainApp/desc.html',param)

def add(request):
    if request.method == 'POST':
        tit = request.POST.get('title')
        des = request.POST.get('desc')
        task = ToDoList(title = tit, desc = des)
        task.save()
        return redirect('main:index')

def delete(request,pk):
    if request.method == 'GET':
        task = ToDoList.objects.get(id = pk)
        task.delete()
        return redirect('main:index')