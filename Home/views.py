#from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render
from scheduleGen.models import Courses, CourseLinks, Majors

class homeactual(TemplateView):
        template_name =  'Home/Homepage.html'





# Create your views here.
