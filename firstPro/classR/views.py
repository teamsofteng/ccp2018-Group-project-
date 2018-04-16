from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from classReview.forms import classReviewForm
#from classReview.models import CourseLinks
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from scheduleGen.models import Majors
class index(TemplateView):
    template_name = 'classR/index.html'
    def get(self,request):
        posts = Majors.objects.filter(majorName="Computer Science")
        post1 = CourseLinks.objects.raw("SELECT scheduleGen_courselinks.courseID, connCourseID, difficultyNode, cohesionNode, overallNode FROM scheduleGen_courses, scheduleGen_courselinks WHERE scheduleGen_courses.courseID = scheduleGen_courselinks.courseID;") 
        args = {'posts':posts,'post1':post1}
        return render(request, self.template_name, args)


# Create your views here.
