
from multiprocessing import context
from rest_framework.response import Response
from polls.models import *
from rest_framework.views import *
from rest_framework.decorators import *
from rest_framework.response import *
from datetime import datetime
from polls.serializers import  *
from django.http import JsonResponse
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    def validate(self, attrs):
        data = super().validate(attrs)

        
        serializer = UserSerializerWithToken(self.user).data
        print(serializer)
        for k, v in serializer.items():
            data[k] = v
        data["detail"]="ok"
        print(data)
        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer     


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUserProfile(request):
    user = request.user
    serializer = UserSerializerWithToken(user, many=False)
    data = request.data
    user.first_name = data['name']
    user.username = data['username']
    user.email = data['email']

   
    user.password = make_password(data['password'])

    user.save()

    return Response(serializer.data)


@api_view(['POST'])
def uploadImage(request):
    

    invite_id = request.data['invite_id']
    invite_image = inviteMarried_request.objects.get(id=invite_id)
    invite_image.image =request.FILES.get('image')
    invite_image.save()
    return Response('Image was uploaded')

@api_view(['POST'])
def invite_request(request): 
    data=request.data
    maleName=data["maleName"]
    femaleName=data["femaleName"]
    location=data["location"]
    clock= data["clock"]
    date=data["date"]

    requests=inviteMarried_request.objects.filter(maleName=maleName,femaleName=femaleName)
    if requests.exists():
        return Response({'result':'تم انشاء الدعوة مسبقا '})
    else:
        p=inviteMarried_request(maleName=maleName,femaleName=femaleName,location=location,clock=clock,date=date)
        p.save()
        return Response({'result':'تم انشاء الدعوة بنجاح'})
@api_view(['POST'])
def details(request): 
    data=request.data
    iid=data["iid"]
    p=inviteMarried_request.objects.get(id=iid)
    serializer=inviteMarried_requestSerializer(p)
    return Response(serializer.data)
@api_view(['GET'])
def my_invites(request):  
    try:
        invites=inviteMarried_request.objects.filter(date__gte=datetime.today()).order_by('-date')
        serializer = inviteMarried_requestSerializer(invites, many=True)
        a=[]
        for i in range(len(invites)):


            a.append({"data":serializer.data[i],"result":"أفراح"})
        return JsonResponse(a,safe=False)    
    except:
        return Response({"data":" ",'result':'ليس هناك اي دعوات'})


        