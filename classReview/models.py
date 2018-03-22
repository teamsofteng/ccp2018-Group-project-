from django.db import models
class CourseLinks(models.Model):
    courseID = models.CharField(max_length=10)
    overallNode = models.FloatField()    
    connCourseID = models.CharField(max_length=10)                                                
    difficultyNode = models.FloatField()           
    #difficultyNodeWeight = models.IntegerField()   
    cohesionNode = models.FloatField()             
    #cohseionNodeWeight = models.IntegerField()   
