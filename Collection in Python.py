#------------------------------------------------List----------------------------------------------------------
a='Rushikesh Babasaheb Akolkar'
print(a[0:10])

list=[100,200,400,101,500,600,700,800,900,200,300,100,200]
print("List of Count = ",list.count(100))

print("List of Index of 500 = ",list.index(500))

print("List of Count = ",list.remove(101))

list.append(505050)

print("List of Count = ",list)

list.sort(reverse=True)

print(list)
# -------------------------------------Tuples-------------------------------------------------------------------
t=(23,34,56,67,67,78)
print(t)
list[0]=99
print(list)

t=tuple(list)
print(t)

t2=sorted(t)
print(t2)

t3=sorted(t2,reverse=True)
print(t3)
#-----------------------------------------------set-------------------------------------------------------------
set={10,10,20,30,40,50}
print(set)

set.add("Python")
print(set)
set.discard("Python")

s1=sorted(set,reverse=True)
print(s1)
#----------------------------------------------day and timing----------------------------------------------------
import datetime as d
today = d.datetime.now()
print("Today's is :",today.day," / ",today.month," / ",today.year)

print(len(set))

a="Rushikesh Babasaheb Akolkar"

print(a)

print("Length of A = ",len(a))