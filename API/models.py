from django.db import models
from django.contrib.auth.models import AbstractUser

class Delegate(AbstractUser):
    email = models.EmailField(blank=False, max_length=255, unique=True)
    username = models.CharField(blank=False, max_length=255, unique=False)
    typeOfDelegate = models.CharField(max_length=255, blank=False, null=True)
    aiesecEmail = models.EmailField(blank=True, max_length=255)
    entity = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["typeOfDelegate", "username"]

class Speaker(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/speakers', null=True, blank=True)
    about = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    social_media = models.CharField(max_length=255, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    speakers = models.ManyToManyField(Speaker, blank=True)
    sessions = models.ManyToManyField("Session", blank=True, related_name="event_sessions")
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name

class Session(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    event = models.ForeignKey(Event, blank=True, null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Score(models.Model):
    username = models.CharField(max_length=255)
    score = models.IntegerField()
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-score']

    def __str__(self):
        return self.username
