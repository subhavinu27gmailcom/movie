from django.http import HttpResponse
from django.shortcuts import render, redirect

from movieapp.forms import modelform
from movieapp.models import Movies


def index(request):
    obj1=Movies.objects.all()
    context={"key1":obj1}
    print(type(obj1))
    print(obj1)
    return render(request,"index.html",context)
def detail(request,movie_id):
    movie=Movies.objects.get(id=movie_id)
    return render(request,"detail.html",{"key2":movie})
def add(request):
    if request.method=="POST":
        name=request.POST.get("name")
        desc=request.POST.get("desc")
        year=request.POST.get("year")
        imag=request.FILES.get("imag")
        movie=Movies(name=name,desc=desc,year=year,imag=imag)
        movie.save()
    return render(request,"add.html")
def update(request,movie_id):
    movobj=Movies.objects.get(id=movie_id)
    form1=modelform(request.POST or None,request.FILES,instance=movobj)
    if form1.is_valid():
        form1.save()
        return redirect ("/")
    return render(request,"update.html",{"key1":movobj,"key2":form1})