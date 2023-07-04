print("Name list of students in Alphapetic order")
record=[]
a=int(input("How many records :"))
for i in range(a):
	name=input("Enter the name :")
	record.append(name)
	record.sort()
print(record)



