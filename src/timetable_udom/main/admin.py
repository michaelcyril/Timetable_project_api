from django.contrib import admin
from .models import *
# Register your models here.

list_m = [Program, Students, Time, College, Venue, TimeTable, Course, TeachingCategory, Instructor, Day]

for a in list_m:
    admin.site.register(a)
