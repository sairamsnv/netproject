from django.db import models

class student(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=200)
    password=models.CharField(max_length=100)


