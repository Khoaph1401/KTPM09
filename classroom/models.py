from django.db import models
from authentication.models import User

class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=100)
    teacher_name = models.CharField(max_length=50)
    course_description = models.TextField()

    def __str__(self):
        return self.course_name