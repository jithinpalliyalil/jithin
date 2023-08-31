from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from .forms import todoform
from.models import task
# Create your views here.
def add (request):
    task2=task.objects.all()
    if request.method == 'POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task1=task(name=name,priority=priority,date=date)
        task1.save()
    return render(request,'home.html',{'task2':task2})

def delete(request,taskid):
    task3=task.objects.get(id=taskid)
    if request.method == 'POST':
        task3.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,upid):
    task4=task.objects.get(id=upid)
    form1=todoform(request.POST or None,instance=task4)
    if form1.is_valid():
        form1.save()
        return redirect ('/')
    return render (request,'update.html',{'form1':form1,'task4':task4})

