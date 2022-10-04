from django.contrib.auth.models import AbstractUser, User
from django.db import models


# Create your models here.
class Event(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    type = models.TextField(null=True, blank=True)
    location=models.TextField(null=True,blank=True)
    startdatetime = models.DateTimeField(null=True, blank=True)
    enddatetime = models.DateTimeField(null= True, blank=True)
    organizer = models.CharField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    photo = models.TextField(null=True, blank=True)
    # participants = models.ManyToManyField(
    #     User, related_name='participants', blank=True)
    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-startdatetime', '-enddatetime']  # descending order

    def __str__(self):
        return self.name

    def users_count(self):
        event_users = self.user_set.all()
        return event_users.count()

    # def last_message_time(self):
    #     room_message = self.message_set.all()[0]
    #     return room_message.updated




class User(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_id= models.IntegerField(null=True, blank=True)
    first_name = models.CharField(null=False, blank=False)
    last_name = models.CharField(null=True, blank=False)  # file attribute in model
    company_name = models.TextField(null=True, blank=False)
    Email = models.TextField(null=True, blank=False)


    class Meta:
        ordering = ['last_name', 'first_name']  # descending order

    def __str__(self):
        return self.name

    def events_count(self):
        user_events = self.event_set.all()
        return user_events.count()


