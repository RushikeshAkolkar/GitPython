from multipledispatch import dispatch as di
@di(int,int)
def sum(a=10,b=20):
    return(a+b)

@di(int,int,int)
def sum(a=10,b=20,c=30):
    return(a+b+c)

@di(int,int,int,int)
def sum(a=10,b=20,c=30,d=40):
    return(a+b+c+d)

print(sum(10,20,30,40))
print(sum(10,20,300))
print(sum(1000,2000))