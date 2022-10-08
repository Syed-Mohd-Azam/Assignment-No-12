# Write a python script to print first N prime numbers.
print()
n=int(input("Enter the value of N to print N prime numbers : "))
for var in range(2,n+1,1):
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
