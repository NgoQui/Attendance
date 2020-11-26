from django.db import models

class Student(models.Model):
    Username=models.CharField(max_length=100,blank=False,null=False)
    email=models.EmailField(max_length=100,blank=False,null=False)
    # Course=models.CharField(max_length=100,blank=False,null=False)
    password=models.CharField(max_length=100,blank=False,null=False)

    def __unicode__(self):
        return self.Username

class Class(models.Model):
    Name=models.CharField(max_length=255,blank=False,null=False)

    def __unicode__(self):
        return self.Name

