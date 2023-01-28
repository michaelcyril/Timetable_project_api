from django.db import models


# Create your models here.

class College(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Program(models.Model):
    college_id = models.ForeignKey(College, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'program {self.name} of {self.college_id.name}'


class Venue(models.Model):
    college_id = models.ForeignKey(College, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'venue {self.name} of {self.college_id.name}'


class Course(models.Model):
    college_id = models.ForeignKey(College, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'course {self.name} of {self.college_id.name}'


class Students(models.Model):
    program_id = models.ForeignKey(Program, on_delete=models.CASCADE)
    year = models.IntegerField()

    def __str__(self):
        return f'{self.program_id.name}{str(self.year)}'


class Time(models.Model):
    time_interval = models.CharField(max_length=200)

    def __str__(self):
        return self.time_interval


class TeachingCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Instructor(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Day(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class TimeTable(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    time_id = models.ForeignKey(Time, on_delete=models.CASCADE)
    day_id = models.ForeignKey(Day, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    instructor_id = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    venue_id = models.ForeignKey(Venue, on_delete=models.CASCADE)
    teaching_category_id = models.ForeignKey(TeachingCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.day_id.name} {self.time_id.time_interval} {self.course_id.name} {self.student_id.program_id.name}{self.student_id.year}'
