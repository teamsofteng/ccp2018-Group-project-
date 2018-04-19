from django.views.generic import TemplateView
from django.shortcuts import render
from scheduleGen.forms import ScheduleForm
from scheduleGen.models import Courses, CourseLinks, Majors
schedule = []
addedCourses = []
semesterCount = 8
creditLimit = 15
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

	def getCourseLinkValue(self, semester, course):
		retVal = 0
		for mainCourse in semester:
			courseLinkData = CourseLinks.objects.get(courseID=mainCourse[0], connCourseID=course)
			retVal += ( courseLinkData.difficultyNode / 3 ) + ( courseLinkData.cohesionNode / 3 ) + ( courseLinkData.overallNode / 3 )
		return retVal

	def post(self, request):
		form = ScheduleForm(request.POST)
		scheduleForm = ScheduleForm()
		global schedule
		global creditLimit
		global addedCourses
		schedule = []

		if form.is_valid():
			print("Self 1: {}".format(self))
			code = form.cleaned_data['searchValueMajor']
			creditLimit = 15
			callBack = Majors.objects.get(majorCode=code)
			result = ''
			mainCourses = callBack.majorCourses.split(',')
			# Place all the core classes into a list
			ctr = 0
			for course in mainCourses:
				schedule.append([])
				self.addCourseToSchedule(ctr, course)
				ctr += 1

			# Check prerequisites for the major courses
			ctr =0
			for semester in schedule:
				prereqs = self.checkPrereqs(semester[0][0])
				if prereqs != None:
					for course in prereqs.split(','):
						if course not in addedCourses:
							self.addCourseToSchedule(ctr-1, course)
				ctr += 1 #iterate each semester

			sideCourses = (callBack.sideCourses).split(',')
			# Remove courses from side courses where we have already added them
			for course in sideCourses:
				if course in addedCourses:
					sideCourses.remove(course)

			ctr = 0
			for semester in schedule:
				coursesAvailableForSemester = []
				coursesAvailableForSemesterLinks = []
				creditsTaken = 0
				for course in semester:
					creditsTaken += course[1]
				for course in sideCourses:
					prereqs = self.checkPrereqs(course)
					if prereqs != None and prereqs in coursesAdded:
						coursesAvailableForSemester.append(course)
						coursesAvailableForSemesterLinks.append(self.getCourseLinkValue(semester, course))
					else:
						coursesAvailableForSemester.append(course)
						coursesAvailableForSemesterLinks.append(self.getCourseLinkValue(semester, course))
				while creditsTaken < creditLimt:
					minimumValue = 1000000
					courseToTake = 'CYBR 1100'
					for course, value in zip(coursesAvailableForSemester, coursesAvailableForSemesterLinks):
						if value < mininmumValue:
							minimumValue = value
							courseToTake = course
					self.addCourseToSchedule(ctr, course)
					if ctr != 7:
						creditsTaken = 0
						for course in semester:
							creditsTaken += course[1]
				ctr += 1

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
			# Create the arguments dictionary and return it with the template and request in the render function
			args = {'scheduleForm':scheduleForm, 'result':result}
			return render(request, self.template_name, args)
