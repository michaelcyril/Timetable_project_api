from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from .serializer import UserSerializer
from django.contrib.auth import authenticate, login, logout
from .token import get_user_token
from .models import User
from .models import *
from django.db.models import Q


# Create your views here.

@api_view(["POST"])
@permission_classes([AllowAny])
def RegisterUser(request):
    if request.method == "POST":
        data = request.data
        username = data['username']
        # user = None
        user = User.objects.filter(username=username)
        if user:
            message = {'message': 'user does exist'}
            return Response(message)

        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            message = {'save': True}
            return Response(message)
        else:
            message = {'save': False}
            return Response(message)
    return Response({'message': "hey bro"})


# {
#     "username":"mike",
#     "email":"mike@gmail.com",
#     "password":"123"
# }

@api_view(["POST"])
@permission_classes([AllowAny])
def LoginView(request):
    username = request.data.get('username')
    password = request.data.get('password')

    myuser = User.objects.values("is_active", "id").get(username=username)
    print(myuser)
    if not myuser['is_active']:
        response = {
            'msg': 'Please visit your admin for more subscription',
        }

        return Response(response)

    user = authenticate(username=username, password=password)
    print(user)

    if user is not None:
        login(request, user)
        user_id = User.objects.values('id').get(username=username)['id']
        # profile_id = Profile.objects.values('id', 'ward_id', 'user_id', 'phone', 'description').get(user_id=user_id)

        response = {
            'msg': 'success',
            # 'profile_id': profile_id,
            'tokens': get_user_token(user),
        }

        return Response(response)
    else:
        response = {
            'msg': 'Invalid username or password',
        }

        return Response(response)


# {
#     "username": "mike",
#     "password": "123"
# }


@api_view(["POST"])
@permission_classes([AllowAny])
def ActivateDeactivateUser(request):
    try:
        user = User.objects.values("id", "is_active").get(id=request.data['user_id'])
        # print(user)
        if user['is_active'] == True:
            us = User.objects.get(id=request.data['user_id'])
            # print("i reach here")
            us.is_active = False
            us.save()
            message = {"change": True}
            return Response(message)

        elif user['is_active'] == False:
            us = User.objects.get(id=request.data['user_id'])
            us.is_active = True
            us.save()
            message = {"change": True}
            return Response(message)

    except:
        message = {"change": False}
        return Response(message)


# {
#     "user_id": 1
# }

@api_view(["POST"])
@permission_classes([AllowAny])
def PostEventView(request):
    try:
        user_id = User.objects.get(id=request.data['user_id'])
        event = Event.objects.create(issued_by=user_id,
                                     title=request.data['title'], description=request.data['description'],
                                     event_date=request.data['event_date'], venue=request.data['venue'],
                                     is_free=request.data['is_free'], amount_requested=request.data['amount_requested'],
                                     site_link=request.data['site_link']
                                     )
        event.save()
        myData = Event.objects.values('id').all()
        mySavedData = [entry for entry in myData]
        if len(mySavedData) > 1:
            e_id = []
            for i in range(0, len(mySavedData) - 1):
                id = mySavedData[i]['id']
                e_id.append(id)
            last_e_id = max(e_id)

        elif len(mySavedData) == 1:
            last_e_id = mySavedData[0]['id']

        else:
            return Response({"message": "Insert event"})

        myEvent = Event.objects.get(id=last_e_id)

        for img in request.data['images']:
            image = img['image']
            ImageToSave = Image.objects.create(asset_id=myEvent, image=image)
            ImageToSave.save()
        message = {"message": "successful saved"}
        return Response(message)
    except:
        message = {"message": "fail to save"}
        return Response(message)


# {
#     "user_id": 1,
#     "description": "bra bra",
#     "event_date": "12-12-2023",
#     "venue": "LRB",
#     "title": "HEY THERE",
#     "is_free": False,
#     "amount_required": 10000,
#     "site_link": "www.facebook.com",
#     "images": [{"image":"hey.png"}, {"image":"hey2.png"}]
# }


@api_view(["POST"])
@permission_classes([AllowAny])
def ChangeActiveView(request):
    try:
        asset = Event.objects.values("id", "is_active").get(id=request.data['event_id'])
        if asset['is_active']:
            event = Event.objects.get(id=request.data['event_id'])
            event.is_active = False
            event.save()
            message = {"change": True}
            return Response(message)

        elif not asset['is_active']:
            event = Event.objects.get(id=request.data['event_id'])
            event.is_active = True
            event.save()
            message = {"change": True}
            return Response(message)

    except:
        message = {"change": False}
        return Response(message)


# {
#     "event_id": 1,
# }


@api_view(["POST"])
@permission_classes([AllowAny])
def PostFeedbackView(request):
    try:
        feed = Feedback.objects.create(sender_name=request.data['sender_name'],
                                       description=request.data['description'])
        feed.save()

    except:
        message = {"message": "fail to send"}
        return Response(message)

    message = {"message": "feedback send"}
    return Response(message)


# {
#     "sender_name": "jackass",
#     "description": "hey this app is complete and functions well more than my expectations"
# }


@api_view(["POST"])
@permission_classes([AllowAny])
def ChangeActiveViewFeedback(request):
    try:
        feed = Feedback.objects.values("id", "is_active").get(id=request.data['feedback_id'])
        if feed['is_active']:
            fd = Feedback.objects.get(id=request.data['feedback_id'])
            fd.is_active = False
            fd.save()
            message = {"change": True}
            return Response(message)

        elif not feed['is_active']:
            fd = Feedback.objects.get(id=request.data['feedback_id'])
            fd.is_active = True
            fd.save()
            message = {"change": True}
            return Response(message)

    except:
        message = {"change": False}
        return Response(message)


# {
#     "feedback_id": 1,
# }


@api_view(["GET"])
@permission_classes([AllowAny])
def getAllUser(request):
    user = User.objects.values('id', 'username', 'email').all()
    return Response({"users": user})


@api_view(["GET"])
@permission_classes([AllowAny])
def getAllEvents(request):
    events = Event.objects.values('id', 'title', 'description',
                                  'issued_by', 'event_date', 'venue',
                                  'is_free', 'amount_requested', 'site_link',
                                  'is_active').filter(is_ctive=True)
    a = [entry for entry in events]
    b = []
    for x in a:
        data = {
            "id": x['id'],
            "title": x['title'],
            "description": x['description'],
            "issued_by": User.objects.values('username').get(id=x['issued_by'])['username'],
            "event_date": x['event_date'],
            "venue": x['venue'],
            "is_free": x['is_free'],
            "mount_requested": x['amount_requested'],
            "site_link": x['site_link'],
            "is_active": x['is_active']
        }
        b.append(data)

    return Response({"events": b})


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def getMyEvents(request):
    user = User.objects.get(username=request.user)
    events = Event.objects.values('id', 'title', 'description',
                                  'issued_by', 'event_date', 'venue',
                                  'is_free', 'amount_requested', 'site_link',
                                  'is_active').filter(issued_by=user)
    a = [entry for entry in events]
    b = []
    for x in a:
        data = {
            "id": x['id'],
            "title": x['title'],
            "description": x['description'],
            "issued_by": User.objects.values('username').get(id=x['issued_by'])['username'],
            "event_date": x['event_date'],
            "venue": x['venue'],
            "is_free": x['is_free'],
            "mount_requested": x['amount_requested'],
            "site_link": x['site_link'],
            "is_active": x['is_active']
        }
        b.append(data)

    return Response({"events": b})


@api_view(["GET"])
@permission_classes([AllowAny])
def getAllFeedback(request):
    feed = Feedback.objects.values('id', 'sender_name', 'description', 'created_at', 'is_active').filter(is_active=True)
    return Response({"feedbacks": feed})
