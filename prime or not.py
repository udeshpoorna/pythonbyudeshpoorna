n=int(input("enter the number to check:"))
for i in range(2,n):
    if n % i==0:
        print("its not a prime number")
        break
else:
    print("its a prime number")