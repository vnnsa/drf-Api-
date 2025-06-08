from .users import UserViewSet
from .tasks import TaskViewSet
from .submissions import SubmissionViewSet
from django.http import HttpResponse
from rest_framework import viewsets
from ..models import Submission
from ..serializers import SubmissionSerializer

def home_view(request):
    return HttpResponse("Welcome to Intern Task API")

class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer


__all__ = ['UserViewSet', 'TaskViewSet', 'SubmissionViewSet']
