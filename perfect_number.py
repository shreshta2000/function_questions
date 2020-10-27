def perfect_number(a):
	while a<1000:
		j=1
		sum=0
		while j<a:
			if a%j==0:
				sum=sum+j
			j=j+1
		if sum==a:
			print(a)
		a=a+1
perfect_number(1)
