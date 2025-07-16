from django.db import models


# Create your models here.

class Skill(models.Model):
    name = models.CharField(max_length=100)  #* Name of the skill
    
    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=100)           #* Name of the project
    description = models.TextField()                  #* Description of the project
    year = models.IntegerField()                      #* Year the project was created
    image = models.ImageField(upload_to='projects/')  #* Image field for project
    repository = models.URLField(blank=True)          #* URL for the project (optional)
    skills = models.ManyToManyField('Skill')          #* Many-to-many relationship with Skill model
    
    def __str__(self):
        return f'{self.name} - {self.year}'