n=int(input('enter a num '))

def fib(x,y):
    print(x)
    y=x+y
    return y
a=0
b=1
for i in range(n):
    k=fib(a,b)
    a=b
    b=k