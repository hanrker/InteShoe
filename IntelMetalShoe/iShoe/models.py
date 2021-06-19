from django.db import models

# Create your models here.
class MetalShoe(models.Model):
    no = models.CharField(max_length=32)
    status = models.ForeignKey("Status",on_delete=models.SET_NULL, null=True)
    type = models.CharField(max_length=32,null=True)
    # def __init__(self,no,status,type=''):
    #     self.no = no
    #     self.status = status
    #     self.type = type
    def new(no,status,type = ''):
        c = MetalShoe(no = no, status = status, type = type)
        c.save()


class Status(models.Model):
    no = models.IntegerField()
    name = models.CharField(max_length=32)
    def p(self):
        print('ss')


class Tag(models.Model):
    no = models.CharField(max_length=8)
    name = models.CharField(max_length=8)
    shoeid = models.ManyToManyField(MetalShoe,through='ShoeTag')

    # def __str__(self):
    #     self.name

class ShoeTag(models.Model):
    metalshoe = models.ForeignKey(MetalShoe,on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag,on_delete= models.CASCADE)
    creatime = models.DateField()
    people = models.CharField(max_length=8)
    infor = models.CharField(max_length=128)