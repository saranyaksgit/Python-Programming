print("Student record using dictionary")
n=int(input("How many data :")) 
d={} 
for i in range(n):
	roll_no=int(input("Enter roll no :"))
	name=input("Enter name :")
	marks=int(input("Enter marks :"))
	d[roll_no]=[name,marks] 
print(d)

