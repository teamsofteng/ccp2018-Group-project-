from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from classReview.forms import classReviewForm
#from classReview.models import CourseLinks
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

class index(TemplateView):
    template_name = 'class/index.html'
    def index1(request):
        query_results = Majors.objects.all()
        mjs = MajorChoice()
        context = {
            'query_results': query_results,
	    'mjs': mjs,
        }
        return render(request,'class/index.html',context)

#class home(TemplateView):
#    template_name =  'class/index.html'
#    def get(self,request):
#        form = classForm()
#        return render(request,self.template_name, {'form': form})
#    def post(self, request):
#        form = classForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('index')


#       return render(request, self.template_name, {'form': form,})




