from django import forms
from scheduleGen.models import Majors

#class classForm(forms.ModelForm):
#    majorCode = models.CharField(max_length=10, primary_key=True)          
#    majorName = models.CharField(max_length=35)                            
#    majorCourses = models.CharField(max_length=500)                        
#    sideCourses = models.CharField(max_length=500)                         
#    electives = models.IntegerField()    
#    class Meta:
#        model =  Majors
#        fields = ('majorCode', 'majorName', 'majorCourses', 'sideCourses', 'electives',)
#class MajorChoice(forms.Form):
#    mj = forms.ModelChoiceField(
#	queryset = Majors.objects.all())

