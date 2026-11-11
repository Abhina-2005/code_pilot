from django.db import models

# Create your models here.

from django.contrib.auth.models import  User

from user.models import User

class Assessment(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    instructions=models.TextField()
    duration=models.PositiveIntegerField()
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('published', 'Published'),
        ('completed', 'Completed'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    creator= models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='assessments'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# •	Assessment — Stores title, description, instructions, duration, status, creator, and relevant timestamps.    

    