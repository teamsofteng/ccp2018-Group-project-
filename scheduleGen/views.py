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
			creditLimit = form.cleaned_data['creditLimit']
			callBack = Majors.objects.get(majorCode=code)
			result = ''

			# Place all the core classes into a list
			ctr = 0
			for course in callBack.majorCourses.split(','):
				if course != '':
					hold = Courses.objects.get(courseID=course)
					creditCount = hold.creditHours
					schedule.append([[course, creditCount]])
					ctr += 1

			for addCourse in callBack.sideCourses.split(','):
				if addCourse != '':
					bestScore = -1		# Score for the best edge in the courseLinks table for a given side course
					bestSemester = -1	# Semester that the class will be paired with
					ctr = 0	# Counts semesters
					for semester in schedule:
						# Determine the number of credits already present in a semester
						semCreditCount = 0
						for classH in semester:
							semCreditCount += int(classH[1])

						course = semester[0][0] # Course ID for the major course will always be in the very first slot
						hold = CourseLinks.objects.get(courseID=course, connCourseID=addCourse) # Returns the link value for the major course and course pair then evaluates
						if hold.overallNode > bestScore and semCreditCount < creditLimit:
							bestScore = hold.overallNode
							bestSemester = ctr

						ctr += 1

					# Addition of the course to the best semester
					if bestScore != -1:
						print('Best')
						creditCalc = (Courses.objects.get(courseID=course)).creditHours
						schedule[bestSemester].append([addCourse, creditCalc])

			# Generate a Readable Text Output
			ctr = 1
			for semester in schedule:
				creditCount = 0
				courseList = ''
				for course, credits in semester:
					creditCount += credits
					courseList += (course + '\n')
				
				courseList += lineDivider + '\n\n'
				result += 'Semester {} | Credit Total:{}\n{}\n'.format(ctr,creditCount,lineDivider)
				result += courseList
				ctr += 1


		args = {'scheduleForm':scheduleForm, 'result':result}
		return render(request, self.template_name, args)


