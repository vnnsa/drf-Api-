from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from .models import User, Task, Submission, Notification
from .serializers import UserSerializer, TaskSerializer, SubmissionSerializer, NotificationSerializer
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Welcome to the Intern Task API")

# Authentication endpoints
@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def logout(request):
    try:
        refresh_token = request.data["refresh"]
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response(status=status.HTTP_205_RESET_CONTENT)
    except Exception as e:
        return Response(status=status.HTTP_400_BAD_REQUEST)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'])
    def assign(self, request, pk=None):
        task = self.get_object()
        user_id = request.data.get('user_id')
        user = User.objects.get(pk=user_id)
        task.assigned_to = user
        task.save()
        Notification.objects.create(user=user, message=f"You have been assigned task: {task.title}")
        return Response({'status': 'assigned'})

    @action(detail=True, methods=['put'])
    def progress(self, request, pk=None):
        task = self.get_object()
        task.status = request.data.get('status', task.status)
        task.save()
        return Response({'status': 'progress updated'})

    @action(detail=True, methods=['post'])
    def submit(self, request, pk=None):
        task = self.get_object()
        serializer = SubmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(task=task, submitted_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['put'])
    def review(self, request, pk=None):
        submission = self.get_object()
        submission.feedback = request.data.get('feedback', submission.feedback)
        submission.status = request.data.get('status', submission.status)
        submission.save()
        return Response({'status': 'review updated'})

class NotificationViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)
    
@api_view(['GET'])
@permission_classes([permissions.IsAdminUser])
def task_stats(request):
    from django.db.models import Count
    stats = Task.objects.values('status').annotate(count=Count('id'))
    return Response(stats)