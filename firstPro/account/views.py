from django.shortcuts import render, redirect
from account.forms import RegistrationForm
def home(request):
	return render(request, 'account/Homepage.html')
def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('http://ec2-35-173-183-216.compute-1.amazonaws.com/')
	else:
		form = RegistrationForm()
		

		args = {'form': form}
		return render(request,'account/register.html',args)
