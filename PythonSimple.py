a=int(input("Enter The Number Which You want to reverse:\n"))
reminder=0
b=a
sum=0
while(b!=0):
    reminder=int(b%10)
    sum=(sum*10)+reminder
    b=int(b/10)
print(sum)
