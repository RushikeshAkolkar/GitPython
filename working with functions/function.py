#void function 
def even_odd(num):
    if num%2==0:
        print(num,"is Even Number")
    else:
        print(num,"is Odd Number")
even_odd(10)
even_odd(15)

#return function
#Function Definition
def isEven(num):
    if num%2 == 0:
        return True;
    else:
        return False;
#Function Calling
result = isEven(11)
print(result)


#sum and avrage of all subjects
def sum(s1,s2,s3,s4,s5,s6):
    total = s1+s2+s3+s4+s5+s6
    return total
def avg(total,count):
    avg = total/count
    return avg
total_marks = sum(44,55,66,77,88,99)
avg_marks = avg(total_marks,6)
print("Total marks: ",total_marks)
print("Avg marks: ",avg_marks)


