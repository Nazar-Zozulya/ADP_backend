from django.db import models

from user_app.models import CustomUser

# Create your models here.


class Course(models.Model):
    image = models.ImageField(upload_to='courses/', blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='author')
    students = models.ManyToManyField(CustomUser, related_name='student', blank=True, null=True)
    

class Lesson(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    text_part = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)    

class Test(models.Model):
    title = models.TextField()
    
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    
    
class AnswerOption(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='options')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)