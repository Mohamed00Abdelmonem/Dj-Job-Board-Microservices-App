from rest_framework import generics
from .serializers import JobSerializer, JobApplySerializer
from .models import Job, JobApply
# from .filters import JobFilter


class JobList(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer



class JobDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer    