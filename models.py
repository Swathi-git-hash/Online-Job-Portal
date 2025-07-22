from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    posted_on = models.DateTimeField(auto_now_add=True)

class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant_name = models.CharField(max_length=255)
    applicant_email = models.EmailField()
    resume = models.TextField()
    applied_on = models.DateTimeField(auto_now_add=True)