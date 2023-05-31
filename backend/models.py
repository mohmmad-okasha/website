import django
from django.db import models


#####################################################################################

class Subjects(models.Model):
    name = models.CharField(max_length=50,unique=True)
    description = models.CharField(max_length=300)
    timestamp = models.CharField(blank=True,max_length=50)

    def __str__(self):
        return self.name #to change object name in admin table

    class Meta:
        ordering= ['id'] #to Sort the values

#####################################################################################

class Links(models.Model):
    subject_id = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    url = models.CharField(max_length=50)
    timestamp = models.CharField(blank=True,max_length=50)

    
    def __str__(self):
        return self.title

    class Meta:
        ordering= ['id']

#####################################################################################

class Settings(models.Model):
    dark_mode = models.BooleanField()
    lang = models.CharField(max_length=50)
    primary_color = models.CharField(max_length=50)
    back_color = models.CharField(max_length=50)

#####################################################################################
