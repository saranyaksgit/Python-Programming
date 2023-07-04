def fact():
	print("Factorial using Function")
	num=int(input("Enter the number :"))
	fact=1
	for i in range(num,1,-1):
		fact=fact*i
	print("The factorial is :",fact)
fact()
