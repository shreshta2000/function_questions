def is_harshad_number(num):
	i=num
	while i>0:
		j=0
		rem=0
		sum=0
		while j<=i:
			rem=num%10
			sum=sum+rem
			num=num//10			
		#reverse=rem*10+rem
		#sum=sum+reverse
		
			j=j+1
		
		i=i+1
	print(sum,i)
	if num%sum==0:
		print(i,"harshad number")
is_harshad_number(100)
