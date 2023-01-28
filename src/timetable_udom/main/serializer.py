from rest_framework import serializers
from .models import *


class TimeTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeTable
        fields = [
            'course_id',
            'time_id',
            'day_id',
            'student_id',
            'instructor_id',
            'venue_id',
            'teaching_category_id'
        ]
        depth = 3
