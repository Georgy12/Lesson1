def cut_cake(parts):
	try:
		return 1/int(parts)
	except (ZeroDivisionError,TypeError,ValueError):
		return"not allowed"
cake=cut_cake([1,2,3])	
print(cake)