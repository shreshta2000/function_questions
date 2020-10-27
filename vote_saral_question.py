def eligible_for_vote(age):
	if age>=18:
		result="you are eligible for vote"
	else:
		result= "you are not eligible for vote"
	return (result)
age=int(input("entre any age  "))
print(eligible_for_vote(age))