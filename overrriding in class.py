from multipledispatch import dispatch
class Mycity:
    a=0
    b=0

    def __init__(self) -> None:
        return 0

    def add1(self,a:int,b:int) :
        print("addition of a and b is ",a+b)

class Mycity1(Mycity):
    a=0
    b=0

    def __init__(self) -> None:
        return 0

    def add(self,a:str,b:str):
        print("Concatination of two String is",a+b)


class Mycity2(Mycity1):
    a=0
    b=0

    def __init__(self) :
        self.a=12
        self.b=30

    def add(self,a:float,b:float):
        print("Addition of two dubble value is = ",a+b)


obj = Mycity1
obj.add1(1,10,20)
obj.add(1,"Rushikesh ","Akolkar")
obj.add(1,5.0,15.6)

obj2=Mycity2()
print("The value's of a & b is",obj2.a,obj2.b,"Respectively")