# Write a python script to calculate HCF of two numbers.
def HCF(a,b):
    l1,l2,hcf=[],[],1
    while(a>=1):
        for e in range(2,a+1,1):
            if int(a%e)==0:
                l1.append(e)
                break
            else:
                continue
        a=a//e
    while(b>=1):
        for e in range(2,b+1,1):
            if int(b%e)==0:
                l2.append(e)
                break
            else:
                continue
        b=b//e
    for e in l1:
        for k in l2:
            if e==k:
                l2.remove(k)
                hcf=hcf*k
                break
    return(hcf)
print("Enter two numbers to calculate HCF between them: ")
num1,num2=int(input("Enter first number : ")),int(input("Enter second number : "))
print("Highest common factor between them is : ",HCF(num1,num2))