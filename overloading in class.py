from multipledispatch import dispatch as d
class Mycity:
    x=None
    a=0
    b=0
    def __init__(self,a) -> None:
        self.x=a

    @d(int,int)
    def add(self,a,b):
        print("addition is :",a+b)
    
    @d(str,str)
    def add(self,a,b):
        print("String after concatination is : ",a+b)

p=Mycity("Ahmednagar")
print("My city is :",p.x)

p.add(10,20)

p.add("Rushikesh ","Babasaheb Akolkar")