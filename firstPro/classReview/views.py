from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from classReview.forms import classReviewForm
from classReview.models import CourseLinks
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

class home(TemplateView):
    template_name =  'classReview/index.html'
    def get(self,request):
        form = classReviewForm()
        return render(request,self.template_name, {'form': form})
    def post(self, request):
        form = classReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
				
        
        return render(request, self.template_name, {'form': form,})
			


