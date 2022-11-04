from django.db import models

# Create your models here.
from django.db import models
from authentication.models import User
from django.utils import timezone


class Assignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    file = models.FileField(null=True, blank=True)
    marks = models.CharField(max_length=10)
    startdate = models.DateField(default=timezone.now())
    enddate = models.DateField(default=timezone.now())

    def __str__(self):
        return self.title


class Exam(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    file = models.FileField(null=True, blank=True)
    marks = models.CharField(max_length=10)
    duration = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title


class AssignmentSubmission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    file = models.FileField(null=True, blank=True)
    marks = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.assignment


class ExamSubmission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    file = models.FileField(null=True, blank=True)
    marks = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.exam