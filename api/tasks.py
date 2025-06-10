from celery import shared_task
from .models import Notification, User

@shared_task
def send_notification(user_id, message):
    user = User.objects.get(id=user_id)
    Notification.objects.create(user=user, message=message)