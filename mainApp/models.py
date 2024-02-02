from django.db import models

choice=((0,"Pending"),(1,"Done"))
class Member(models.Model):
    id=models.AutoField(primary_key=True)
    photo=models.ImageField(upload_to="uploads",default='',null=True,blank=True)
    name=models.CharField(max_length=100,default='',null=True,blank=True)
    email=models.EmailField(default='',null=True,blank=True)
    phone=models.CharField(max_length=10,default='',null=True,blank=True)
    email=models.EmailField(default='',null=True,blank=True)
    latitude=models.TextField(default='',null=True,blank=True)
    longitude=models.TextField(default='',null=True,blank=True)
    device_id=models.TextField(default='',null=True,blank=True)
    device_token=models.TextField(default='',null=True,blank=True)
    status=models.CharField(max_length=100,default='Active',null=True,blank=True)
    verification=models.IntegerField(choices=choice,default=0,null=True,blank=True)
    def __str__(self):
        return (self.name)+" "+str(self.verification)
    
class Family_Member(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.CharField(max_length=100,default='',null=True,blank=True)
    photo=models.ImageField(upload_to="uploads",default='',null=True,blank=True)
    name=models.CharField(max_length=100,default='',null=True,blank=True)
    email=models.EmailField(default='',null=True,blank=True)
    phone=models.CharField(max_length=10,default='',null=True,blank=True)
    relation=models.CharField(max_length=100,default='',null=True,blank=True)
    latitude=models.TextField(default='',null=True,blank=True)
    longitude=models.TextField(default='',null=True,blank=True)
    device_id=models.CharField(max_length=1000,default='',null=True,blank=True)
    device_token=models.TextField(default='',null=True,blank=True)

    def __str__(self):
        return (self.name)


class Notification(models.Model):
    id=models.AutoField(primary_key=True)
    device_id=models.CharField(max_length=10000,default='',null=True,blank=True)
    status=models.CharField(max_length=100,default='Active',null=True,blank=True)


class LonLat(models.Model):
    id=models.AutoField(primary_key=True)
    device_id=models.CharField(max_length=1000,default='',null=True,blank=True)
    latitude=models.TextField(default='',null=True,blank=True)
    longitude=models.TextField(default='',null=True,blank=True)

    def __str__(self):
        return (self.device_id)

class New_Update(models.Model):
    id=models.AutoField(primary_key=True)
    app_link=models.CharField(max_length=10000,default='',null=True,blank=True)
    status=models.CharField(max_length=10,default="Pending",null=True,blank=True)