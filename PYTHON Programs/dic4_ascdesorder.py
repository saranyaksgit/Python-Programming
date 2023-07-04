print("Dictionary in Ascending order & Descending order")
n=int(input("How many records :"))
student_dict={}
for i in range(n):
	name=input("Enter student's name :")
	roll_no=int(input("Enter student's roll_number :"))
	mark=input("Enter student's mark :")
	student_dict[roll_no]=[name,mark]
	
print("Records in ascending order")
print(sorted(student_dict.values()))

print("Records in descending order")
print(sorted(student_dict.values(),reverse=True))
