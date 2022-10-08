# Write a python script to reverse a number.
print()
n=int(input("Enter a number : "))
rev=0
while(n>0):
    rev=int(rev*10)+int(n%10)
    n=int(n/10)
print("Reverse of a number is : ",rev)
print()