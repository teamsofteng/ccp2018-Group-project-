from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from classReview.forms import classReviewForm
#from classReview.models import CourseLinks
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from scheduleGen.models import Majors
from scheduleGen.models import CourseLinks
class index(TemplateView):
    template_name = 'classW/index.html'
    def get(self,request):
        posts = Majors.objects.filter(majorName="Biomedical Informatics & Bioinformatics")
        post1 = CourseLinks.objects.raw('SELECT DISTINCT courseID, 1 id,connCourseID, difficultyNode, cohesionNode, overallNode FROM scheduleGen_courselinks WHERE scheduleGen_courselinks.courseID IN (SELECT DISTINCT(courseID) FROM scheduleGen_courselinks, scheduleGen_majors WHERE majorName = "Biomedical Informatics & Bioinformatics" AND (instr(majorCourses, courseID)>0 OR instr(sideCourses, courseID) >0 OR instr(electives,courseID) > 0));') 
        args = {'posts':posts,'post1':post1}
        return render(request, self.template_name, args)


# Create your views here.
