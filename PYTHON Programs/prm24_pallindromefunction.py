print("Palindrome Using Function")
def pal():
	num=int(input("Enter a number :"))
	temp=num
	reverse=0
	while(num>0):
    		rem=num%10
    		reverse=reverse*10+rem
    		num=int(num/10)
	if(temp==reverse):
    		print(reverse,"The number is palindrome")
	else:
    		print(reverse,"Not a palindrome")
pal()
