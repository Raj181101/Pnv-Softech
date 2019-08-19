from django.shortcuts import render
from stpolice.models import Psstate,Distps,Mops

# Create your views here.
def Stp(request):
    stp=Psstate.objects.all()
    return render(request,'stpolice/stp.html',{'form':stp})

def Dtp(request,id):
    stp=Psstate.objects.get(id=id)
    #name=stp.state
    #print(stp)
    dtp=Distps.objects.filter(pss=stp)
    return render(request,'stpolice/dtp.html',{'form':dtp})

def Mtp(request,id):
    dtp=Distps.objects.get(id=id)
    mtp=Mops.objects.filter(dps1=dtp)
    id=dtp.pss.id
    return render(request,'stpolice/mtp.html',{'form':mtp,'dtp':dtp,'id':id})