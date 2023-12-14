from django.db import models

# Create your models here.

class Studentdeatils(models.Model):
    name=models.CharField(max_length=50)
    age=models.TextField(blank=True,null=True)
    place=models.TextField()
    address=models.TextField()

    def __str__(self):
        return self.name
    