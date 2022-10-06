from django.shortcuts import render

# Create your views here.
def ForLoop(request):
    d={'name':'SUBHRAJIT SWAIN','n':[1,2,3,4,5,6,7,8,9]}
    return render(request,'ForLoop.html',d)