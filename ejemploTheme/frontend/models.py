from django.db import models
from django.utils import timezone

# Create your models here.

class Student(models.Model):
    #id = models.CharField(max_length=10)
    group = models.PositiveIntegerField(max_length=1)
    list_number = models.PositiveIntegerField(max_length=2)
    student_id = models.CharField(max_length=10, default='')

    def __str__(self):
        return f"{self.group} - {self.list_number}"



class Questions(models.Model):
    #id = models.CharField(max_length=10)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    answer1a = models.PositiveIntegerField(max_length=2)
    answer1b = models.PositiveIntegerField(max_length=2)
    answer2a = models.PositiveIntegerField(max_length=2)
    answer2b = models.PositiveIntegerField(max_length=2)
    answer3a = models.PositiveIntegerField(max_length=2)
    answer3b = models.PositiveIntegerField(max_length=2)
    answer4a = models.PositiveIntegerField(max_length=2)
    answer4b = models.PositiveIntegerField(max_length=2)
    correctAnswerA = models.PositiveIntegerField(max_length=2)
    correctAnswerB = models.PositiveIntegerField(max_length=2)
    student_answerA = models.PositiveIntegerField(max_length=2)
    student_answerB = models.PositiveIntegerField(max_length=2)
    responseTime = models.PositiveIntegerField(max_length=3)
    level = models.PositiveIntegerField(max_length=1)
    difficulty = models.PositiveIntegerField(max_length=1)
    dateTime = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.question}"


