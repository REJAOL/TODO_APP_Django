from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tasks(models.Model):
    status_choices=[
        ('C', 'COMPLETED'),
        ('P', 'PENDING')
    ]
    priority_choices=[
        ('5', 'Normal'),
        ('10', 'High')
    ]
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    status = models.CharField(max_length=2, choices = status_choices)
    user = models.ForeignKey(User , on_delete = models.CASCADE)
    priority = models.CharField(max_length=2, choices = priority_choices)
    create_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
