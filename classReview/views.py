from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from classReview.forms import classReviewForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from scheduleGen.models import CourseLinks
from scheduleGen.models import Courses
from django.core.exceptions import ObjectDoesNotExist

class home(TemplateView):
	template_name =  'classReview/index.html'
	def get(self,request):
		form = classReviewForm()
		return render(request,self.template_name, {'classReviewForm': form, 'reply':'Please enter your review below'})
	def post(self, request):
		form = classReviewForm(request.POST)
		courseid =request.POST.get('courseID')
		connCourseid = request.POST.get('connCourseID')

		courseid = 'FAKE 1000'
		overallnode = 50
		connCourseid = 'FAKE 1000'
		difficultynode = 50
		cohesionnode = 50


		if form.is_valid():
			courseid = form.cleaned_data['courseID']
			overallnode = form.cleaned_data['overallNode']
			connCourseid = form.cleaned_data['connCourseID']
			difficultynode = form.cleaned_data['difficultyNode']
			cohesionnode = form.cleaned_data['cohesionNode']
			try:

				callBack = CourseLinks.objects.get(courseID=courseid, connCourseID=connCourseid)
				callBack.overallNode = (overallnode + int(callBack.overallNode))/2
				callBack.difficultyNode = (difficultynode + callBack.difficultyNode)/2
				callBack.cohesionNode = (cohesionnode + callBack.cohesionNode)/2

			except ObjectDoesNotExist:
				callBack = CourseLinks(courseID=courseid, connCourseID=connCourseid, overallNode=overallnode, difficultyNode=difficultynode, cohesionNode=cohesionnode )

			callBack.save()
			result = 'Review submitted successfully! Thank you!'
			return render(request, self.template_name, {'classReviewForm': classReviewForm(), 'reply':result})
		else:
			return render(request, self.template_name, {'classReviewForm': form, 'reply':'Please enter valid data'})
