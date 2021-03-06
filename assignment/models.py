from django.db import models

# Create your models here.


class Assignment(models.Model):
    staffname = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
    desc = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.name


class Answer(models.Model):
    staffname = models.CharField(max_length=200, null=True)
    assignmentname = models.CharField(max_length=200, null=True)
    regno = models.CharField(max_length=20)
    answer = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.regno


class Document(models.Model):
    staffname = models.CharField(max_length=255, blank=True)
    assignmentname = models.CharField(max_length=255, blank=True)
    regno = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/%Y/%m/%d/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.regno
