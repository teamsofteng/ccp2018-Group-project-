from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from classReview.forms import classReviewForm
#from classReview.models import CourseLinks
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from scheduleGen.models import CourseLinks
class home(TemplateView):
    template_name =  'classReview/index.html'
    def get(self,request):
        form = classReviewForm()
        return render(request,self.template_name, {'classReviewForm': form})
    def post(self, request):
        form = classReviewForm(request.POST)
        if form.is_valid():
            courseID = request.POST.get('courseID','')
            overallNode = request.POST.get('overallNode','')
            connCourseID = request.POST.get('connCourseID','')
            difficultyNode = request.POST.get('difficultyNode','')
            cohesionNode = request.POST.get('cohesionNode','')
            obj = CourseLinks(courseID = courseID, overallNode = overallNode, connCourseID = connCourseID, difficultyNode= difficultyNode, cohesionNode = cohesionNode)
            obj.save()
            return redirect('index')

        return render(request, self.template_name, {'classReviewForm': form,})


