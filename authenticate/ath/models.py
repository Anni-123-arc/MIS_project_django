from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField(null=True)  # Make the year field nullable
    contact = models.CharField(max_length=100, default='')
    image = models.ImageField(upload_to='student_images/', default='', blank=True)
    
    def __str__(self):
        return self.name + self.contact  



