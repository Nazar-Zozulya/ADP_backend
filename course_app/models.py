from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


class Course(models.Model):
    image = models.ImageField(upload_to='courses/', blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    students = models.ManyToManyField('user_app.User', related_name='courses', blank=True)
    
    def __str__(self):
        return self.name
    
    

class Lesson(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    text_part = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)    
    
    def __str__(self):
        return self.name



class Test(models.Model):
    title = models.TextField()
    
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    
    
class AnswerOption(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='options')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name