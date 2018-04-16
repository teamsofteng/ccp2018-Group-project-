from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from classReview.forms import classReviewForm
#from classReview.models import CourseLinks
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from scheduleGen.models import Majors
class index(TemplateView):
    template_name = 'class/index.html'
    def get(self,request):
        posts = Majors.objects.filter(majorName="Computer Science")
        post1 = Majors.objects.filter(majorName="Cyber Security")
        post2 = Majors.objects.filter(majorName="Management Information Systems")
        post3 = Majors.objects.filter(majorName="IT Innovation")
        post4 = Majors.objects.filter(majorName="Biomedical Informatics & Bioinformatics")
	
        args = {'posts':posts, 'post1':post1,'post2':post2,'post3':post3,'post4':post4}
        return render(request, self.template_name, args)
     
    

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




