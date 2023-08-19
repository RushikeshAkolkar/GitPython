from multipledispatch import dispatch
@dispatch(int,int)
def sum(a,b):
	t=0
	t=a+b
	return t

@dispatch(int,int,int)
def sum(a,b,c):
	t=0
	t=a+b+c
	return t


print(sum(1,2))

print(sum(1,2,3))