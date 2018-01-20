from django.shortcuts import render,HttpResponse


# Create your views here.
def home(request):
    name = 'Brian Karanja'
    age = 21
    number = [1,2,3,4,5]
    args= {'Myname':name,'age':age,'number':number}
    return render(request,'account/login.html',args)
