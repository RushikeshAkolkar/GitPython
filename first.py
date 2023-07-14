a=int(input("\nPlease Inter Number To check Reverse"))
temp =a
sum=0
b=0;
while(temp!=0):
    b=temp%10
    print(sum)
    sum=sum*10+b
    temp=temp/10
    
print(sum)