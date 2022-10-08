# Write a python script to print all Prime numbers between two given numbers (both values inclusive).
print()
print("Enter two values to print all prime numbers between them : (both inclusive) ")
n1,n2=int(input()),int(input())
if n1>=2 and n2>=2:
    n1,n2=n1,n2
    for var in range(n1,n2+1,1):
        i,count=2,0
        while(i<var):
            if var%i==0:
                count=count+1
                break
            else:
                i=i+1
                continue
        if count==0:
           print(var,end=" ")
        print()
elif n1<2 and n2>=2:
    n1,n2=2,n2
    for var in range(n1,n2+1,1):
        i,count=2,0
        while(i<var):
           if var%i==0:
            count=count+1
            break
           else:
            i=i+1
            continue
        if count==0:
            print(var,end=" ")
    print()   
elif n1<2 and n2<2:
    print("Sorry no prime numbers in this range.")
else:
    print()