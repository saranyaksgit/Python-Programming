print("Perfect number")
num=int(input("Enter the number :"))
sum=0
for i in range(1,int((num/2)+1),1):
	if(num%i==0):
		sum=sum+i 	 	
if(num==sum):
	print(num,"is a Perfect Number")
else:
	print(num,"is not a Perfect Number")
