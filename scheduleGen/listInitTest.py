courseP = [1, 2, 3, 4]
course = 1

preRequisiteCoursePlacement = [] # List of three membered lists [ [course links best to worst], [corresponding semesters], credit hours ]
coursePlacement = [] # Three membered list [ [course links best to worst], [corresponding semesters], credit hours ]

for x in courseP:
	preRequisiteCoursePlacement.append([ [], [], x ])

coursePlacement = [ [], [], course ]

print(preRequisiteCoursePlacement)
print("\n")
print(coursePlacement)