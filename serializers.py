from rest_framework import serializers
from .models import Job, Application

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '_all_'

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '_all_'