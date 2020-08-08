from django.db import models
from datetime import datetime


OPTION = (
    ('America/Los_Angeles','America/Los_Angeles'),
    ('Asia/Kolkata', 'Asia/Kolkata'),
)

class Category(models.Model):
    """Get name and timzone"""
    real_name = models.CharField(max_length=100)
    tz = models.CharField(max_length=50, choices=OPTION)

    def __str__(self):
        return self.real_name



class Activity(models.Model):
    """Store Data particular category"""
    category = models.ManyToManyField(Category, related_name='activity_periods')
    start_time = models.DateTimeField(default=datetime.now())
    end_time = models.DateTimeField(default=datetime.now())

    def __decode__(self):
        return self.start_time
