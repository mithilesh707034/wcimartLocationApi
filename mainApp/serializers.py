from rest_framework import serializers
from .models import *

class MemberSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    photo=serializers.ImageField(max_length=None,use_url=True,allow_null=True,required=False)
    name=serializers.CharField(max_length=100)
    email=serializers.EmailField()
    phone=serializers.CharField(max_length=10)
    latitude=serializers.CharField(max_length=1000)
    longitude=serializers.CharField(max_length=1000)
    device_id=serializers.CharField(max_length=10000,default='')
    device_token=serializers.CharField(max_length=10000)
    status=serializers.CharField(max_length=10000)
    verification=serializers.CharField(max_length=20)
    def create(self,validatedData):
        return Member.objects.create(**validatedData)
    

class Family_MemberSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    admin=serializers.CharField(max_length=10)
    photo=serializers.ImageField(max_length=None,use_url=True,allow_null=True,required=False)
    name=serializers.CharField(max_length=100)
    email=serializers.EmailField()
    phone=serializers.CharField(max_length=10)
    relation=serializers.CharField(max_length=100)
    latitude=serializers.CharField(max_length=1000)
    longitude=serializers.CharField(max_length=1000)
    device_id=serializers.CharField(max_length=10000)
    device_token=serializers.CharField(max_length=10000)
    
    def create(self,validatedData):
        return Member.objects.create(**validatedData)


class NotificationSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    device_id=serializers.CharField(max_length=10000)
    status=serializers.CharField(max_length=10000)
    
    def create(self,validatedData):
        return Notification.objects.create(**validatedData)
    

class LonLatSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    device_id=serializers.CharField(max_length=10000)
    latitude=serializers.CharField(max_length=1000)
    longitude=serializers.CharField(max_length=1000)
    
    def create(self,validatedData):
        return LonLat.objects.create(**validatedData)



class New_UpdateSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    app_link=serializers.CharField(max_length=10000)
    status=serializers.CharField(max_length=10)
    
    def create(self,validatedData):
        return New_Update.objects.create(**validatedData)