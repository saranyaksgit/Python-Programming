print("Armstrong or Not")
a=int(input("Enter the number :"))
b=0
k=a
s=0
while(k>0):
	b=k%10
	s=s+(b*b*b)
	k=int(k/10)
if(s==a):
	print(a,"is an Amstrong")
else:
	print(a,"is not Amstrong")
