from django import forms
from classReview.models import CourseLinks

class classReviewForm(forms.ModelForm):
    courseID = forms.CharField(max_length=10)
    overallNode = forms.FloatField()
    connCourseID = forms.CharField(max_length=10)
    difficultyNode = forms.FloatField()
    #difficultyNodeWeight = forms.IntegerField()
    cohesionNode = forms.FloatField()
    #cohseionNodeWeight = forms.IntegerField()

    class Meta:
        model =  CourseLinks
        fields = ('courseID', 'overallNode', 'connCourseID', 'difficultyNode', 'cohesionNode',)
