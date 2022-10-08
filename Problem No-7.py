# Write a python script to check whether a given pair of numbers are co-Prime numbers or not.
def coprime(num1,num2):
    l1,l2=[],[]
    for e in range(1,num1,1):
        if int(num1%e)==0:
            l1.append(e)
    for e in range(1,num2+1,1):
        if int(num2%e)==0:
            l2.append(e)
    s1,s2=set(l1),set(l2)
    s=s1.intersection(s2)
    print("Given numbers are comprime numbers !")if s==set([1]) else print("Given numbers are not coprime!")
print("Please enter two numbers to check whether they are coprime numbers or not: ")
a,b=int(input("Enter first number: ")),int(input("Enter second number: "))
coprime(a,b)