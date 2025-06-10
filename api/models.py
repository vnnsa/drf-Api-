from django.db import models
from django.contrib.auth.models import AbstractUser


#username:binishhaa
#pw:2003@1209bin

class User(AbstractUser):
    ROLE_CHOICES = (('admin', 'Admin'), ('manager', 'Manager'), ('intern', 'Intern'))
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    assigned_to = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='tasks')
    status = models.CharField(max_length=20, default='Not Started')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tasks')

class Submission(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='submissions/', null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    feedback = models.TextField(blank=True)
    status = models.CharField(max_length=20, default='Pending')
    submitted_at = models.DateTimeField(auto_now_add=True)

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)