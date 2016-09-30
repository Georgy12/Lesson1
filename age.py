age=int(input('your age'))
if age>2 and 7>age:
	print('nursery school')
elif age<18 and age>7:
	print('school')
elif age>18 and age<24:
	print('university')
elif age>24:
	print('go to work')
else:
	print('unknown input')