from rest_framework.response import Response
from django.db.models import Q
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny
from .serializer import *
from .models import *


# Create your views here.

@api_view(["POST"])
@permission_classes([AllowAny])
def SearchView(request):
    student_id = request.data['student_id']
    day_id = request.data['day_id']
    x = Students.objects.get(id=student_id)
    print(x)
    y = Day.objects.get(id=day_id)
    print(y)
    mydata = TimeTable.objects.values('id', 'time_id', 'day_id', 'course_id', 'student_id', 'instructor_id',
                                      'venue_id').filter(
        Q(student_id=x) & Q(day_id=y))
    tt = []
    for a in mydata:
        d = Day.objects.values("name").get(id=a['day_id'])['name']
        t = Time.objects.values("time_interval").get(id=a['time_id'])['time_interval']
        c = Course.objects.values('name').get(id=a['course_id'])['name']
        i = Instructor.objects.values('name').get(id=a['instructor_id'])['name']
        v = Venue.objects.values('name').get(id=a['venue_id'])['name']
        timetable = {'id': a['id'], 'day': d, 'time': t, 'course': c, 'student_id': a['student_id'], 'instructor': i,
                     'venue': v}
        tt.append(timetable)

    print(tt)
    return Response({'data': tt})


# {
#     "student_id":1,
#     "day_id":1
# }


@api_view(["GET"])
@permission_classes([AllowAny])
def Student(request):
    data = Students.objects.values('id', 'program_id', 'year').all()
    return Response({'data': data})


@api_view(["GET"])
@permission_classes([AllowAny])
def Days(request):
    data = Day.objects.values('id', 'name').all()
    return Response({'data': data})


@api_view(["GET"])
@permission_classes([AllowAny])
def Prog(request):
    data = Program.objects.values('id', 'name', 'college_id').all()
    return Response({'data': data})


@api_view(["GET"])
@permission_classes([AllowAny])
def AllTimeTable(request):
    mydata = TimeTable.objects.values('id', 'time_id', 'day_id', 'course_id', 'student_id', 'instructor_id',
                                      'venue_id').all()
    tt = []
    for a in mydata:
        d = Day.objects.values("name").get(id=a['day_id'])['name']
        t = Time.objects.values("time_interval").get(id=a['time_id'])['time_interval']
        c = Course.objects.values('name').get(id=a['course_id'])['name']
        i = Instructor.objects.values('name').get(id=a['instructor_id'])['name']
        v = Venue.objects.values('name').get(id=a['venue_id'])['name']
        timetable = {'id': a['id'], 'day': a['day_id'], 'time': t, 'course': c, 'student_id': a['student_id'], 'instructor': i,
                     'venue': v}
        tt.append(timetable)

    print(tt)
    return Response({'data': tt})
