from django import forms
from classReview.models import CourseLinks

class classReviewForm(forms.Form):
    courseID = forms.CharField(max_length=10)
    overallNode = forms.FloatField(max_value=100,min_value=0)
    connCourseID = forms.CharField(max_length=10)
    difficultyNode = forms.FloatField(max_value=100,min_value=0)
    #difficultyNodeWeight = forms.IntegerField()
    cohesionNode = forms.FloatField(max_value=100,min_value=0)
    #cohseionNodeWeight = forms.IntegerField()

    class Meta:
        model =  CourseLinks
        fields = ('courseID', 'overallNode', 'connCourseID', 'difficultyNode', 'cohesionNode',)
