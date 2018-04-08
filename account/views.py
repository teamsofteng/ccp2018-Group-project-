from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
def home(request):
	return render(request, 'account/Homepage.html')
def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/account')
	else:
		form = UserCreationForm()
		

		args = {'form': form}
		return render(request,'account/register.html',args)
