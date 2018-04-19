from django.views.generic import TemplateView
from django.shortcuts import render
from scheduleGen.forms import ScheduleForm
from scheduleGen.models import Courses, CourseLinks, Majors
schedule = []
addedCourses = []
semesterCount = 8
lineDivider = '--------------------------------------------------------'

class Index(TemplateView):
	template_name = 'scheduleGen/home.html'
	result = 'Error Finding Your Major'
	lineDivider = '--------------------------------------------------------'
	semesterCount = 8

	def get(self, request):
		scheduleForm = ScheduleForm()
		result = 'Schedule output will be displayed here.'
		args = {'scheduleForm':scheduleForm, 'result':result}
		return render(request, self.template_name, args)

#-------------------------
# Post Methods
#-------------------------
	def checkPrereqs(self, courseName):
		courseData = Courses.objects.get(courseID=courseName)
		return courseData.prerequisites

	def addCourseToSchedule(self, semester, course):
		global addedCourses
		global schedule
		courseData = Courses.objects.get(courseID=course)
		addedCourses.append(course)
		schedule[semester].append([course, courseData.creditHours])

	def post(self, request):
		form = ScheduleForm(request.POST)
		scheduleForm = ScheduleForm()
		global schedule
		global creditLimit
		schedule = []

		if form.is_valid():
			code = form.cleaned_data['searchValueMajor']
			creditLimit = 15
			callBack = Majors.objects.get(majorCode=code)
			result = ''
			mainCourses = callBack.majorCourses.split(',')
			# Place all the core classes into a list
			ctr = 0
			for course in mainCourses:
				if course != None:
					schedule.append([])
					self.addCourseToSchedule(course)
					ctr += 1

			# Check prerequisites for the major courses
			ctr =0
			for semseter in schedule:
				prereqs = self.checkPrereqs(semester[0][0])
				if prereqs != None:
					for course in prereqs.split(','):
						if course not in addedCourses:
							self.addCourseToSchedule(ctr-1, course)
				ctr += 1 #iterate each semester
			


			# Assemble the schedule into a readable output string and assign to result
			ctr = 1
			result = ""
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

			else:
				# Non-Normal Length Error out for now
				result = "Issues with majorCourses definition in database\nSemCount: {}".format(len(schedule))
			
			# Create the arguments dictionary and return it with the template and request in the render function
			args = {'scheduleForm':scheduleForm, 'result':result}
			return render(request, self.template_name, args)