from django import forms


class classReviewForm(forms.Form):
    courseID = forms.CharField(max_length=10)
    overallNode = forms.FloatField()    
    connCourseID = forms.CharField(max_length=10)                                        
    difficultyNode = forms.FloatField()           
    #difficultyNodeWeight = forms.IntegerField()   
    cohesionNode = forms.FloatField()             
    #cohseionNodeWeight = forms.IntegerField()   

