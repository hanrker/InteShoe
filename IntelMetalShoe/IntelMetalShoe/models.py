from django.db import models
class MetalShoe(models.Model):
    no = models.CharField(max_length=32)
    status = models.ForeignKey('Status')

class Status(models.Model):
    no = models.IntegerField(max_length=3)
    name = models.CharField(max_length=32)