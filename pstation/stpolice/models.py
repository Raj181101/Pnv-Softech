from django.db import models
# Create your models here.

class Psstate(models.Model):
    state=models.CharField(max_length=30)
    
    def __str__(self):
        return self.state

class Distps(models.Model):
    dps=models.CharField(max_length=30)
    pss=models.ForeignKey(Psstate,on_delete=models.CASCADE)

    def __str__(self):
        return self.dps

class Mops(models.Model):
    dps1=models.ForeignKey(Distps,on_delete=models.CASCADE,related_name="dps1")
    mps=models.CharField(max_length=30)
    pname=models.CharField(max_length=20)
    noofemp=models.IntegerField()

    def __str__(self):
        return self.mps
