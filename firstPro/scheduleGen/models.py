from django.db import models

class Courses(models.Model):
	courseID = models.CharField(max_length=10, primary_key=True) 		#ex CSCI300
	courseName = models.CharField(max_length=75)						#ex Introduction to Java

class CourseLinks(models.Model):
	class Meta:
		unique_together = (('courseID', 'connCourseID'),)
	courseID = models.CharField(max_length=10)							#ex CSCI3000
	connCourseID = models.CharField(max_length=10)						#ex CSCI3350
	overallNode = models.FloatField()										#ex 25 (numbered 0-100 where higher is better) Overall rating (combination of difficulty and cohesion scores)
	difficultyNode = models.FloatField()										#ex 25 (numbered 0-100 where higher is better) Difficulty when these courses are paired
	difficultyNodeWeight = models.IntegerField()								# This will be the number of entries that make the data point (So if 100 reviews created thsi value the weight will be 100)
	cohesionNode = models.FloatField()										#ex 25 (numbered 0-100 where higher is better) Relation comparing course content
	cohseionNodeWeight = models.IntegerField()									# This will be the number of entries that make the data point (So if 100 reviews created thsi value the weight will be 100)

class Majors(models.Model):
	majorCode = models.CharField(max_length=10, primary_key=True)		#ex CompSci
	majorName = models.CharField(max_length=35)							#ex Computer Science
	majorCourses = models.CharField(max_length=500)						# Core courses in the major (Maybe a progression through 4 years in that order)
	sideCourses = models.CharField(max_length=500)						# Required courses that are not in the core courses
	electives = models.IntegerField()									# Number of Electives needed to finish the major
