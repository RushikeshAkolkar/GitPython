num = int(input("Please Enter A Number Which You Want to Cheack Wheather It is a Prime or not? :"))

temp=num
sum=0
n=0

while(temp!=0):
    n=int(temp%10)
    sum=sum+n*n*n
    print(sum)
    temp=int(temp/10)

if(sum==num):
    print(f"            {sum} : The Number is Armstrong Number")
else:
    print(f"            {sum} : The Number is Not Armstrong")