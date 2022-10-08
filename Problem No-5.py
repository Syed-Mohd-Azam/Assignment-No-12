# Write a python script to find next prime number of a given number.
n=int(input("Enter a number to find next prime number : "))
num,count=n+1,0
while(True):
    cout=0
    for e in range(2,num,1):
        if int(num%e)==0:
            cout=cout+1
            count=count+1
            break
        else:
            continue
    if cout==0:
        print("Next prime number is : ",num)
        break
    else:
        num=num+1 