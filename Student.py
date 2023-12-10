class Student:
    def __init__(self,a,b,c) -> None:
        id=a
        name=b
        address=c
    id = None
    name = None
    address = None

n=int(input("How many student do you want:"))
s=Student
s1=(25,'Rushikesh Babasaheb Akolkar','Pune')

for i in range(1,n):
    s1.id = int(input("Please Enter The id :"))
    s1.name = input("Please Enter The Name of Student :")
    s1.address = input("Please Enter the Address of Student :")

for i in range(1,n):
    s.id = int(input("Please Enter The id :"))
    s.name = input("Please Enter The Name of Student :")
    s.address = input("Please Enter the Address of Student :")

#Printing values in Student class

print("Value Of Student is \n")

for i in range(1,n):
    print("Student id : ",s.id,"Student name is",s.name,"Student Address is",s.address)