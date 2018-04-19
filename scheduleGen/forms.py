from django import forms

class ScheduleForm(forms.Form):
	majorChoices = [('','Select a Major'),('compsci','Computer Science')]
	searchValueMajor = forms.CharField(label='Select Your Major',widget=forms.Select(choices=majorChoices))
