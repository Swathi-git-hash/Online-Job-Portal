from rest_framework import viewsets
from .models import Job, Application
from .serializers import JobSerializer, ApplicationSerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all().order_by('-posted_on')
    serializer_class = JobSerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all().order_by('-applied_on')
    serializer_class = ApplicationSerializer