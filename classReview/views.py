from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from classReview.forms import classReviewForm
from classReview.models import CourseLinks
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

class home(TemplateView):
    template_name =  'classReview/index.html'
    def classReviewView(request):
        if request.method == 'POST':
            form = classReviewForm(request.POST)
            if form.is_valid():
                courseID = request.POST.get('courseID','')
                overallNode = request.POST.get('overallNode','')                
                connCourseID = request.POST.get('connCourseID','')
                difficultyNode = request.POST.get('difficultyNode','')
                cohesionNode = request.POST.get('cohesionNode','')
                class_obj = CourseLinks(courseID = courseID, overallNode = overallNode ,connCourseID = connCourseID, difficultyNode = difficultyNode, cohesionNode = cohesionNode)
                class_obj.save()
                return redirect('classReview:classReview')
				
        else:
            form = classReviewForm()
        return render(request, self.template_name, {'form': form,})
			


