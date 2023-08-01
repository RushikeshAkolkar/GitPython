while True:
    print("1.Add")
    print("2.Sub")
    print("3.Mul")
    print("4.Div")
    option = int(input("Enter Option Which do You want to Do Operation from List:"))
    if option == 1:
       a=int(input("Enter First Value:"))
       b=int(input("Enter Second Value:"))
       c=a+b
       print("Addition Value of c==",c)
    elif option == 2:
       a=int(input("Enter First Value:"))
       b=int(input("Enter Second Value:"))
       c=a-b
       print("Addition Value of c==",c) 
    elif option == 3:
       a=int(input("Enter First Value:"))
       b=int(input("Enter Second Value:"))
       c=a*b
       print("Multiplication Value of c==",c) 
    elif option == 4:
       a=int(input("Enter First Value:"))
       b=int(input("Enter Second Value:"))
       c=a/b
       print("Division Value of c==",c) 
    else:
       print("Not Identifiede")
       break