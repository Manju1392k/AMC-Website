from django.db import models

# Create your models here.
class StudentDetails(models.Model):
    Name = models.CharField(max_length=100)
    Age = models.CharField(max_length=2)
    Father_Name = models.CharField(max_length=100)
    Group = models.CharField(max_length=4)
    Location = models.CharField(max_length=150)
    Mole_One = models.CharField(max_length=70)
    Mole_Two = models.CharField(max_length=70)

    def __str__(self):
        return self.Name
