# Write a python script to calculate LCM of two numbers.
def LCM(a,b):
    l1,l2,lcm=[],[],1
    while(a>1):
        for e in range(2,a+1,1):
            if int(a%e)==0:
                l1.append(e)
                break
            else:
                continue
        a=int(a//e)
    while(b>1):
        for e in range(2,b+1,1):
            if int(b%e)==0:
                l2.append(e)
                break
            else:
                continue
        b=int(b//e)
    for e in l1:
        for k in l2:
            if e==k:
                lcm=lcm*k
                l2.remove(k)
                break
            else:
                continue
        else:
            lcm=lcm*e
    for e in l2:
        lcm=lcm*e
    return(lcm)
print("Enter two numbers to find LCM between them : ")
print("LCM between the given numbers is : ",LCM(int(input("Enter first number: ")),int(input("Enter second number: "))))