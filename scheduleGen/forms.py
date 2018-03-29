from django import forms

class ScheduleForm(forms.Form):
	majorChoices = [('','Select a Major'),('compsci','Computer Science'),('bioi','Bioinformatics')]
	searchValueMajor = forms.CharField(label='Select Your Major',widget=forms.Select(choices=majorChoices))
	creditLimit = forms.IntegerField(min_value=3,max_value=30)
