from django.db import models
from django.contrib.auth.models import User
from jsonfield import JSONField

# Create your models here.
class Student(models.Model):
    objects = models.Manager()
    user = models.OneToOneField('auth.user',default="", on_delete=models.CASCADE)
    name = models.CharField(default="", max_length=128)
    email = models.EmailField()
    isStudent = models.BooleanField(default=True)
    isVerified = models.BooleanField(default=False)
    auth_token = models.CharField(default="", max_length=128)

    def __str__(self):
        return self.name


class Resume(models.Model):
    objects = models.Manager()
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    address = models.CharField(blank=True, null=True, max_length=128)
    mob = models.CharField(blank=True, null=True, max_length=10)
    skills = models.TextField(blank=True, null=True)
    pic = models.ImageField(upload_to="student/", blank=True, null=True)
    college = models.CharField(blank=True, null=True, max_length=128)
    grad_year = models.CharField(blank=True, null=True, max_length=10)
    cgpa = models.CharField(blank=True, null=True, max_length=5)
    resume_file = models.FileField(upload_to="student/resume/", blank=True, null=True)

    def __str__(self):
        return self.student.name


    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Resume'
        verbose_name_plural = 'Resumes'


class Certificate(models.Model):
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    std_id = models.IntegerField()

    title = models.CharField(max_length=1000, blank=True, null=True)
    company_name = models.CharField(max_length=1000, blank=True, null=True)
    complition_year = models.IntegerField()
    credential = models.CharField(max_length=100, blank=True, null=True)
    certificate_file = models.FileField(upload_to="student/certificate/", blank=True, null=True)

    def __str__(self):
        return self.title