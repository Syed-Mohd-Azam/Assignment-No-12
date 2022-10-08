# Write a python script to print first N terms of a Fibonacci series.
n=int(input ("Enter the value of N to print first N terms of a Fibonacci series : "))
if n<=0:
    print()
    print("Are you kidding me ! ")
elif n==1:
    print()
    print(0)
elif n==2:
    print(0,1,sep=" ",end=" ")
else :
    a,b,i=0,1,1
    print(a,b,sep="  ",end="  ")
    while(i<=(n-2)):
        c=a+b
        print(c,end="  ")
        a,b,i=b,c,(i+1)
print()
print()