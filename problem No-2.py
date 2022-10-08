# Write a python script to check whether a given number is Prime or not.
print()
n=int(input("Enter a number : "))
i,count=2,0
while(i<n):
    if n%i==0:
        count=count+1
        break
    else:
        i=i+1
        continue
if count==0:
    print(" Prime Number !")
else:
    print("Not a prime number ! ")
print()