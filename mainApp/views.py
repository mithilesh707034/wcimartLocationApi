from django.shortcuts import render,HttpResponse,redirect
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .serializers import *
import json
import io
import requests


@csrf_exempt
def add_member(Request):
    if (Request.method=="POST"):
        data=Member()
        data.photo=Request.FILES.get('photo')
        data.name=Request.POST.get('name')
        data.email=Request.POST.get('email')
        data.phone=Request.POST.get('phone')
        data.latitude=Request.POST.get('latitude')
        data.longitude=Request.POST.get('longitude')
        data.device_id=Request.POST.get('device_id')
        if(Member.objects.filter(phone=data.phone)):
            msg={'status':False,'message':"Record Already Exit..."}
            jsonData=JSONRenderer().render(msg)
            return HttpResponse(jsonData,content_type="application/json")
        elif(Family_Member.objects.filter(phone=data.phone)):
            msg={'status':False,'message':"Record Already Exit..."}
            jsonData=JSONRenderer().render(msg)
            return HttpResponse(jsonData,content_type="application/json")
        else:
            data.save()
            msg={'status':True,'message':"Record Added Successfully..."}
            jsonData=JSONRenderer().render(msg)
            return HttpResponse(jsonData,content_type="application/json")
          

@csrf_exempt
def get_member(Request):
     if (Request.method=="POST"):
          phone=Request.POST.get('phone')
          device_token=Request.POST.get('device_token')

          try:
               data=Member.objects.get(phone=phone)
               if(data):
                 data.device_token=device_token
                 data.save()
                 if(data.verification == 0):
                    msg={'status':False,'message':"Your verification is Pending, Please Contact at 9999127533"}
                    jsonData=JSONRenderer().render(msg)
                    return HttpResponse(jsonData,content_type="application/json")
                 else:
                    dataSerializer=MemberSerializer(data,many=False)
                    realData={'status':True,'message':"Data Got Successfully...",'data':[dataSerializer.data]}
                    return HttpResponse(json.dumps(realData),content_type="application/json")

          except:
               msg={'status':False,'message':"Invalid Phone Number ..."}
               jsonData=JSONRenderer().render(msg)
               return HttpResponse(jsonData,content_type="application/json")


@csrf_exempt
def get_all_member(Request):
    
    data=Member.objects.all().order_by('id').reverse()
    if(data):
      dataSerializer=MemberSerializer(data,many=True)
      realData={'status':True,'message':"Data Got Successfully...",'data':dataSerializer.data}
      return HttpResponse(json.dumps(realData),content_type="application/json")
    else:
        msg={'status':False,'message':"No Data Found ..."}
        jsonData=JSONRenderer().render(msg)
        return HttpResponse(jsonData,content_type="application/json")

@csrf_exempt
def update_member(Request):
    if (Request.method=="POST"):
        phone=Request.POST.get('phone')
        try:
            data=Member.objects.get(phone=phone)
            if(data):
                if(Request.FILES.get('photo')):
                    data.photo=Request.FILES.get('photo')
                data.name=Request.POST.get('name')
                data.email=Request.POST.get('email')
                data.phone=phone
                data.latitude=Request.POST.get('latitude')
                data.longitude=Request.POST.get('longitude')
                data.device_id=Request.POST.get('device_id')
                if (Request.POST.get('status')):
                   data.status=Request.POST.get('status')
                data.save()
                msg={'status':True,'message':"Record Updated Successfully..."}
                jsonData=JSONRenderer().render(msg)
                return HttpResponse(jsonData,content_type="application/json")
        except:
               msg={'status':False,'message':"No Data Found ..."}
               jsonData=JSONRenderer().render(msg)
               return HttpResponse(jsonData,content_type="application/json")



@csrf_exempt
def add_family_member(Request):
    if (Request.method=="POST"):
        data=Family_Member()
        data.admin=Request.POST.get('admin')
        data.photo=Request.FILES.get('photo')
        data.name=Request.POST.get('name')
        data.email=Request.POST.get('email')
        data.phone=Request.POST.get('phone')
        data.relation=Request.POST.get('relation')
        data.latitude=Request.POST.get('latitude')
        data.longitude=Request.POST.get('longitude')
        data.device_id=Request.POST.get('device_id')
        m=Family_Member.objects.filter(phone=data.phone)
        if(Member.objects.filter(phone=data.phone)):
            msg={'status':False,'message':"Record Already Exit..."}
            jsonData=JSONRenderer().render(msg)
            return HttpResponse(jsonData,content_type="application/json")
        elif(Family_Member.objects.filter(phone=data.phone)):
            msg={'status':False,'message':"Record Already Exit..."}
            jsonData=JSONRenderer().render(msg)
            return HttpResponse(jsonData,content_type="application/json")
        else:
            m=int(len(Family_Member.objects.filter(admin=data.admin)))
            if(m<=10):
              data.save()
              msg={'status':True,'message':"Record Added Successfully..."}
              jsonData=JSONRenderer().render(msg)
              return HttpResponse(jsonData,content_type="application/json")
            else:
              msg={'status':False,'message':"You already have added 10 Member..."}
              jsonData=JSONRenderer().render(msg)
              return HttpResponse(jsonData,content_type="application/json")
          

@csrf_exempt
def get_family_member(Request):
     if (Request.method=="POST"):
          phone=Request.POST.get('phone')
          try:
               data=Family_Member.objects.get(phone=phone)
               if(data):
                 dataSerializer=Family_MemberSerializer(data,many=False)
                 realData={'status':True,'message':"Data Got Successfully...",'data':[dataSerializer.data]}
                 return HttpResponse(json.dumps(realData),content_type="application/json")
          except:
               msg={'status':False,'message':"Invalid Phone Number ..."}
               jsonData=JSONRenderer().render(msg)
               return HttpResponse(jsonData,content_type="application/json")


@csrf_exempt
def get_all_family_member(Request):
    admin=Request.POST.get('admin')
    data=Family_Member.objects.filter(admin=admin).order_by('id').reverse()
    if(data):
      dataSerializer=Family_MemberSerializer(data,many=True)
      realData={'status':True,'message':"Data Got Successfully...",'data':dataSerializer.data}
      return HttpResponse(json.dumps(realData),content_type="application/json")
    else:
        msg={'status':False,'message':"No Data Found ..."}
        jsonData=JSONRenderer().render(msg)
        return HttpResponse(jsonData,content_type="application/json")

@csrf_exempt
def update_family_member(Request):
    if (Request.method=="POST"):
        device_id=Request.POST.get('device_id')
        try:
            data=Family_Member.objects.get(device_id=device_id)
            if(data):
                if(Request.FILES.get('photo')):
                    data.photo=Request.FILES.get('photo')
                if(Request.POST.get('name')):
                   data.name=Request.POST.get('name')
                if(Request.POST.get('email')):
                   data.email=Request.POST.get('email')
                if(Request.POST.get('relation')):
                   data.relation=Request.POST.get('relation')
                if(Request.POST.get('phone')):
                   data.phone=Request.POST.get('phone')
                if(Request.POST.get('latitude')):
                    data.latitude=Request.POST.get('latitude')
                if(Request.POST.get('longitude')):
                   data.longitude=Request.POST.get('longitude')
                data.device_id=Request.POST.get('device_id')
                data.save()
                msg={'status':True,'message':"Record Updated Successfully..."}
                jsonData=JSONRenderer().render(msg)
                return HttpResponse(jsonData,content_type="application/json")
        except:
               msg={'status':False,'message':"No Data Found ..."}
               jsonData=JSONRenderer().render(msg)
               return HttpResponse(jsonData,content_type="application/json")

@csrf_exempt
def login_family_member(Request):
     if (Request.method=="POST"):
          phone=Request.POST.get('phone') 
          device_id=Request.POST.get('device_id')
          device_token=Request.POST.get('device_token')
          try:
               data=Family_Member.objects.get(phone=phone)
               if(data):
                 data.device_id=device_id
                 data.device_token=device_token
                 data.save()
                 dataSerializer=Family_MemberSerializer(data,many=False)
                 realData={'status':True,'message':"Data Got Successfully...",'data':[dataSerializer.data]}
                 
                 title=data.name+" 🔐Lgoin Recently🗝️"
                 message=""
                 p=Member.objects.get(phone=data.admin)
                 resgistration  = [p.device_token]
                 send_notification(resgistration , title , message,)
                 return HttpResponse(json.dumps(realData),content_type="application/json")
          except:
               msg={'status':False,'message':"Invalid Phone Number ..."}
               jsonData=JSONRenderer().render(msg)
               return HttpResponse(jsonData,content_type="application/json")




#Sending Notification to Partner
def send_notification(registration_ids , message_title , message_desc):
    fcm_api = "AAAAyUn6oT8:APA91bEK1H56v4L9Jv8_AsMCtWPFNp39VB_08Kju5p_n9GkzyIEK40oZYbqXQ-kewYcic9G7mg79OoHJy7hl-Nuj44miFM7uwoRXg11dG_v2NnXg4zFevZB4zL4Bl0dwoZHKXx4SRkQa"
    url = "https://fcm.googleapis.com/fcm/send"
    
    headers = {
    "Content-Type":"application/json",
    "Authorization": 'key='+fcm_api}

    payload = {
        "registration_ids" :registration_ids,
        "priority" : "high",
        "notification" : {
            "body" : message_desc,
            "title" : message_title,
            "image" : "https://www.hindudharmrakshasabha.com/static/logo.png",
            # "icon": "https://yt3.ggpht.com/ytc/AKedOLSMvoy4DeAVkMSAuiuaBdIGKC7a5Ib75bKzKO3jHg=s900-c-k-c0x00ffffff-no-rj",
            
        }
    }

    result = requests.post(url,  data=json.dumps(payload), headers=headers )
    print(result.json())

@csrf_exempt
def send(Request):
    if(Request.method=="POST"):
        phone=Request.POST.get('phone')
     
        try:
           data=Family_Member.objects.get(phone=phone)
           ad=Member.objects.get(phone=data.admin)
           title="⚠️ Help Me ⚠️"
           message="Please Help Me😨.\n I am in ⚠️ Danger ⚠️"
           n=Notification()
           n.device_id=data.device_id
           n.save()
           p=Family_Member.objects.filter(admin=data.admin)
           for item in p:
            if(item.phone != data.phone):
                resgistration  = [item.device_token]
                send_notification(resgistration , title , message)
            #sending
           resgistration  = [ad.device_token]
           send_notification(resgistration , title , message)
        except:
            data=Member.objects.get(phone=phone)
            title="⚠️ Help Me ⚠️"
            message="Please Help Me😨.\n I am in ⚠️ Danger ⚠️"
            n=Notification()
            n.device_id=data.device_id
            n.save()
            p=Family_Member.objects.filter(admin=phone)
            for item in p:
                resgistration  = [item.device_token]
                send_notification(resgistration , title , message)
        
        msg={'status':True,'message':"Notification sent successfully ..."}
        jsonData=JSONRenderer().render(msg)
        return HttpResponse(jsonData,content_type="application/json")

@csrf_exempt
def view_notification(Request):
    data=Notification.objects.all().order_by('id').reverse()
    if(data):
      dataSerializer=NotificationSerializer(data,many=True)
      realData={'status':True,'message':"Notification Received Successfully...",'data':dataSerializer.data}
      return HttpResponse(json.dumps(realData),content_type="application/json")



@csrf_exempt
def update_notification(Request):
    if Request.method=="POST":
        id=Request.POST.get('id')
        data=Notification.objects.get(id=id)
        data.status="Done"
        data.save()

        dataSerializer=NotificationSerializer(data,many=False)
        realData={'status':True,'message':"Notification updated Successfully...",'data':[dataSerializer.data]}
        return HttpResponse(json.dumps(realData),content_type="application/json")





@csrf_exempt
def add_longlat(Request):
    if (Request.method=="POST"):
        data=LonLat()
        data.device_id=Request.POST.get('device_id')
        data.latitude=Request.POST.get('latitude')
        data.longitude=Request.POST.get('longitude')
        if(LonLat.objects.filter(device_id=data.device_id)):
            msg={'status':False,'message':"Record Already Exit..."}
            jsonData=JSONRenderer().render(msg)
            return HttpResponse(jsonData,content_type="application/json")
        else:
            data.save()
            msg={'status':True,'message':"Record Added Successfully..."}
            jsonData=JSONRenderer().render(msg)
            return HttpResponse(jsonData,content_type="application/json")
          

@csrf_exempt
def update_longlat(Request):
    if (Request.method=="POST"):
        device_id=Request.POST.get('device_id')
        try:
            data=LonLat.objects.get(device_id=device_id)
            if(data):
                data.latitude=Request.POST.get('latitude')
                data.longitude=Request.POST.get('longitude')
                data.device_id=Request.POST.get('device_id')
                data.save()
                msg={'status':True,'message':"Record Updated Successfully..."}
                jsonData=JSONRenderer().render(msg)
                return HttpResponse(jsonData,content_type="application/json")
        except:
               msg={'status':False,'message':"No Data Found ..."}
               jsonData=JSONRenderer().render(msg)
               return HttpResponse(jsonData,content_type="application/json")

      

@csrf_exempt
def get_longlat(Request):
     if (Request.method=="POST"):
          device_id=Request.POST.get('device_id')
          try:
               data=LonLat.objects.get(device_id=device_id)
               if(data):
                 dataSerializer=LonLatSerializer(data,many=False)
                 realData={'status':True,'message':"Data Got Successfully...",'data':[dataSerializer.data]}
                 return HttpResponse(json.dumps(realData),content_type="application/json")
          except:
               msg={'status':False,'message':"Invalid Device ID ..."}
               jsonData=JSONRenderer().render(msg)
               return HttpResponse(jsonData,content_type="application/json")


@csrf_exempt
def delete_family_member(Request):
     if (Request.method=="POST"):
          phone=Request.POST.get('phone')
          try:
               data=Family_Member.objects.get(phone=phone)
               if(data):
                 data.delete()
                 realData={'status':True,'message':"Member Deleted Successfully..."}
                 return HttpResponse(json.dumps(realData),content_type="application/json")
          except:
               msg={'status':False,'message':"Member Not Found..."}
               jsonData=JSONRenderer().render(msg)
               return HttpResponse(jsonData,content_type="application/json")


@csrf_exempt
def new_update(Request):
    data=New_Update.objects.all()
    if(data):
      dataSerializer=New_UpdateSerializer(data,many=True)
      realData={'status':True,'message':"New Update Available...",'data':dataSerializer.data}
      return HttpResponse(json.dumps(realData),content_type="application/json")
    else:
        msg={'status':False,'message':"No Update Available..."}
        jsonData=JSONRenderer().render(msg)
        return HttpResponse(jsonData,content_type="application/json")


@csrf_exempt
def get_single_update(Request):
    id=Request.POST.get('id')
    data=New_Update.objects.get(id=id)
    if(data):
      data.status="Done"
      data.save()
      dataSerializer=New_UpdateSerializer(data,many=False)
      realData={'status':True,'message':"New Update Available...",'data':[dataSerializer.data]}
      return HttpResponse(json.dumps(realData),content_type="application/json")
    else:
        msg={'status':False,'message':"No Update Available..."}
        jsonData=JSONRenderer().render(msg)
        return HttpResponse(jsonData,content_type="application/json")
