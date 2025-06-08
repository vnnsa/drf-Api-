from django.db import models
from django.contrib.auth.models import AbstractUser


#username:binishhaa
#pw:2003@1209bin

class User(AbstractUser):
    pass

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Submission(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    solution = models.TextField(
        default="",
        help_text="The solution submitted by the user"
    )
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='pending')
    feedback = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Submission by {self.user.username} for {self.task.title}"

    class Meta:
        ordering = ['-submitted_at']
        verbose_name = 'Submission'
        verbose_name_plural = 'Submissions'

    def save(self, *args, **kwargs):
        # Custom save logic can be added here if needed
        super().save(*args, **kwargs)