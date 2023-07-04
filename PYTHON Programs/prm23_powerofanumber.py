print("Power of a Number")
def pow(num,exp):
	if(exp==1):
		return(num)
	if(exp!=1):
		return(num*pow(num,exp-1))
num=int(input("Enter the Number :"))
exp=int(input("Enter the Power :"))
print("Result:",pow(num,exp))
