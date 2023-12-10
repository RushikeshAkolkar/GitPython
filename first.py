a=int(input("\nPlease Inter Number To check WHeather it is palindrom or not ?"))
temp =a
sum=0
b=0;
while(temp!=0):
    b=int(temp%10)
    print(sum)
    sum=sum*10+b
    temp=int(temp/10)
    
print(sum)