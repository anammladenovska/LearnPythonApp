from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Lesson(models.Model):
    name = models.CharField(max_length=300, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    video = models.CharField(max_length=500)
    presentation = models.CharField(max_length=500)
    homework = models.CharField(max_length=500)


class Materials(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=False)


class Forum(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

