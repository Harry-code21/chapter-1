
def f(num1,num2):
    return num1+num2

a=int(input("enter 1st number : "))
b=int(input("enter 2nd number : "))
print(f(a,b))



def odd_even(num):
    if num%2 ==0:
        return "even"
    return "odd"    
num=int(input("enter a number : "))
print(odd_even(num))



def pali(name):
    rev=name[::-1]
    if name==rev:
        print(f"{name} is pallindrome")
    else:    
        print(f"{name} is not pallindrome")     
name=input("enter the name : ")
pali(name)


n=int(input("enter value of n upto which you want to ...."))
def fib(n):
    a=0
    b=1
    if n==1:
        print(a)
    elif n==2:
        print(a, b)
    else:
        print(a,b,end=" ")
        for i in range(n-2):
            c=a+b                        # 0+1    2
            a=b                          # a=1   1
            b=c                          # b=1     2
            print(b,end=" ")             # 0 1 1 2 3 5

fib(n)






