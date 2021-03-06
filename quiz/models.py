from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from accounts.models import Student


class Course(models.Model):
    course_name = models.CharField(max_length=50)
    question_number = models.PositiveIntegerField()
    time = models.IntegerField(help_text="duration of the quiz in minutes")
    total_marks = models.PositiveIntegerField()
    is_published = models.BooleanField(('Has been published?'), default=False, null=False)

    def __str__(self):
        return self.course_name


class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    question = models.CharField(max_length=600)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    cat = (('Option1', 'Option1'), ('Option2', 'Option2'), ('Option3', 'Option3'), ('Option4', 'Option4'))
    answer = models.CharField(max_length=200, choices=cat)

    def __str__(self):
        return f"{self.course} - {self.question}  - {self.answer}"


class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    level = models.ForeignKey(Course, on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()


def __str__(self):
    return f"{self.Level} - {self.student} - {self.marks}"
