a=int(input("Enter A Number to check the Number is palindrom or not :"))
reminder=0
b=a
sum=0
while(b!=0):
    reminder=int(b%10)
    sum=(sum*10)+reminder
    b=int(b/10)

if sum==a:
	print(f"The number is Palindrom:",sum)
else:
	print("The Number is Not Palindrom:",sum)