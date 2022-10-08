# Write a python script to print all Prime numbers under 100.
print()
for var in range(2,100,1):
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