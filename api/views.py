from rest_framework import viewsets
from .models import User, Task, Submission
from .serializers import UserSerializer, TaskSerializer, SubmissionSerializer
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from api.models import Submission

def home_view(request):
    return HttpResponse("Welcome to the Intern Task API")
    

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    permission_classes = [IsAuthenticated]