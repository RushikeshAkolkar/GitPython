class Student:
    id = None
    name = None
    address = None

n=int(input("How many student do you want:"))
s=Student

for i in range(1,n):
    s.id = int(input("Please Enter The id :"))
    s.name = input("Please Enter The Name of Student :")
    s.address = input("Please Enter the Address of Student :")

#Printing values in Student class

print("Value Of Student is \n")

for i in range(1,n):
    print("Student id : ",s.id,"Student name is",s.name,"Student Address is",s.address)