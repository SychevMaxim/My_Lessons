student_info = input('Введите информацию о студенте через пробел (имя, фамилия, город, место учёбы, оценки): ').split()
student = dict()
student['Имя'] = student_info[0]
student['фамилия'] = student_info[1]
student['город'] = student_info[2]
student['место учёбы'] = student_info[3]
student['оценки'] = []
for i_grade in student_info[4:]:
	student['оценки'].append(int(i_grade))
for i_info in student:
	print(i_info, '-', student[i_info])