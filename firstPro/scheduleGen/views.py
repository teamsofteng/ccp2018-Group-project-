from django.views.generic import TemplateView
from django.shortcuts import render
from scheduleGen.forms import ScheduleForm
from scheduleGen.models import Courses, CourseLinks, Majors

class Index(TemplateView):
		template_name = 'scheduleGen/home.html'

		def get(self, request):
			scheduleForm = ScheduleForm()

			result = 'Schedule output will be displayed here.'
			args = {'scheduleForm':scheduleForm, 'result':result}
			return render(request, self.template_name, args)

		def post(self, request):
			form = ScheduleForm(request.POST)
			scheduleForm = ScheduleForm()
			result = 'Error Finding Your Major'
			lineDivider = '--------------------------------------------------------'
			schedule = []

			if form.is_valid():
				code = form.cleaned_data['searchValueMajor']
				callBack = Majors.objects.get(majorCode=code)
				result = ''

				# Place all the core classes into a list
				ctr = 0
				for course in callBack.majorCourses.split(','):
					schedule.append([course])
					ctr += 1
				
				# Now Iterate through the classes to find what core classes are most closely related	

				# Generate a Readable Text Output
				ctr = 0
				for x in schedule:
					ctr += 1
					result += 'Semester {}\n{}\n'.format(ctr, lineDivider)
					for y in x:
						result += y + '\n'
					result += lineDivider + '\n\n'


			args = {'scheduleForm':scheduleForm, 'result':result}
			return render(request, self.template_name, args)
