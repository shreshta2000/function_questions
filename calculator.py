def calculator(number_x,number_y,operation):
	if operation =="+":
		result=number_x+number_y
	elif operation=="-":
		result=number_x-number_y
	elif operation=="*":
		result=number_x*number_y
	elif operation=="/":
		result=number_x/number_y
	else:
		result("invalid! operation")
	return result
number_x=int(input("entre any number    "))
number_y=int(input("entre any number    "))
operation=input("entre any sign    ")
print(calculator(number_x,number_y,operation))