#------------------------------------------------List----------------------------------------------------------

list=[100,200,400,101,500,600,700,800,900,200,300,100,200]

print("List of Count = ",list.count(100))

print("List of Index of 500 = ",list.index(500))

print("List of Count = ",list.remove(101))

list.append(505050)

print("List of Count = ",list)

list.sort(reverse=True)

print(list)

print(100 in list)

a=101

if a not in list:
    list.append(a)
    print("Element is added into List :",a)

else:
    print("Element Already Exiscted in List:")

for i in list:
    print(i)

#-------------------------------------Tuples-------------------------------------------------------------------

t=(23,34,56,67,67,78)
print(t)

print(type(t))

list[0]=99
print(list)

t=tuple(list)
print(t)

t2=sorted(t)
print(t2)

list.sort(reverse=True)

t3=sorted(t2,reverse=True)
print(t3)

# max and min
print(max(t))
print(min(t))

#concating
t1 = ('Angular','React')
t2 = ('Python','Django')
print(t1+t2)

# indexing
t = (44, 77, 55, 66, 88, 99)
print(t.index(55))
print(t.index(99))

#count
t = (44, 77, 55, 66, 88, 99, 55, 44, 44)
print(t.count(44))
print(t.count(55))


#-----------------------------------------------set-------------------------------------------------------------
set={10,10,20,30,40,50}
print(set)

set.add("Python")
print(set)

set.discard("Python")

s1=sorted(set,reverse=True)
print(s1)

# set defining and printing

s = {44,55,66,77,88,99,44}

print(type(s))
print(s)


#----------------------------------------------dictionary----------------------------------------------------

d={}

d[100]="Jones"
d[200]="Alice"
d[300]="Smith"

print(d)

d={100:"Jones",200:"Alice",300:"Smith"}
print(d)

d={100:"Jones",200:"Alice",300:"Shiv"}
print(d.items())

for k,v in d.items():
    print(k,"----",v)

d={100:"Jones", 200:"Alice", 300:"Smith"}
print(d.values())
print(d.keys())
for v in d.values():
    print(v)

#clear function
d={100:"Jones",200:"Alice",300:"Smith"}
print(d)
d.clear()
print(d)

#delete keys and value get automatically deleted 
d={100:"Jones",200:"Alice",300:"Smith"}
print(d)
del d[100]
print(d)

#update it's value by using key
d={100:"Jones",200:"Alice",300:"Smith"}
print(d)
d[100]="Susi"
print(d)
d[400]="Mike"
print(d)

#copy by using copy meythod
d1={100:"Jones",200:"Alice",300:"Shiv"}
d2 = d1.copy()
print(d1)
print(d2)

#add student details and marks
marks_report = {}
size = int(input("Enter number of students U want to add: "))
i=1

while i <= size:
    print("Enter Student ",i)
    name=input("Enter Student Name: ")
    marks=input("Enter Student Marks: ")
    marks_report[name] = marks
    i=i+1

print("Name of Student","\t","% of marks")
print("===============","\t","==========")

for name,marks in marks_report.items():
    print(name,"\t\t\t",marks)






#----------------------------------------------day and timing----------------------------------------------------
import datetime as d
today = d.datetime.now()

print("Today's is :",today.day," / ",today.month," / ",today.year)

print("Today's is :",today.hour," : ",today.minute," : ",today.second)

print(len(set))

a="Rushikesh Babasaheb Akolkar"
ab="Hrishikesh Babasaheb AKolkar"
print(a,"       ",ab)

print("Length of A = ",len(a),"Length of AB = ",len(ab))

for b in a :
    print(b)