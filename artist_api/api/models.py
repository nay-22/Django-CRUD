from django.db import models
from django.contrib.auth.models import User

class Work(models.Model):
    link = models.CharField(max_length=255, null=True)
    WORK_CHOICES = [
        ('YT', 'Youtube'),
        ('IG', 'Instagram'),
        ('OT', 'Other'),
    ]
    work_type = models.CharField(max_length=2, choices=WORK_CHOICES, null=True)

class Artist(models.Model):
    name = models.CharField(max_length=255, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    works = models.ManyToManyField(Work)


