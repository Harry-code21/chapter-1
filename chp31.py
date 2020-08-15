#looping
n=int(input("enter value of n : "))
i=0
sum=0
while i<=n:
    sum=sum+i
    i=i+1
print(sum)


n=input("enter any value")
sum=0
i=0
l=len(n)
while i<l:
    sum=sum+int(n[i])
    i=i+1
print(sum)


for i in range(1,11):
    print(i)


n=int(input("enter n"))
for i in range(0,n+1):
    print(i)



