from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    issued_by = models.ForeignKey(User, on_delete=models.CASCADE)
    event_date = models.DateField(null=True)
    venue = models.CharField(max_length=20)
    is_free = models.BooleanField(default=False)
    amount_requested = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    site_link = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title} at {self.venue} {self.event_date}'


class Image(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="uploads/", null=True, blank=True)

    def __str__(self):
        return 'demo'


class Feedback(models.Model):
    sender_name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.sender_name} fb: {self.description}'
