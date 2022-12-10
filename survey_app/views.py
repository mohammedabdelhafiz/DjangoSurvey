from django.shortcuts import render, redirect



def index(request):
    return render(request,'create.html')

def second(request):
  
        username=request.POST["username"]
        dojolocation=request.POST["dojolocation"]
        favlang=request.POST["favlang"]
        comment=request.POST["comment"]


        context = {
            'username' : username , 
            'dojolocation' : dojolocation,
            'favlang' : favlang,
            'comment' : comment
        }
        return render(request, 'apply.html' , context)