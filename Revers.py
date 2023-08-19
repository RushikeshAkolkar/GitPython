#num=123
#rev=0
#digit=0
#while (num!=0):
#    digit = num%10
#    if(digit>0):
#        rev=rev*10+digit
#        num=num/10
#    print(rev)
#print(rev)


num = 1234
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number: " + str(reversed_num))