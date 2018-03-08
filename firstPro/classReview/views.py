from django.views.generic import TemplateView
from django.shortcuts import render
from scheduleGen.models import Courses, CourseLinks, Majors

def home(request):
	return render(request, 'index.html')

