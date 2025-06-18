p=int(input("enter positive number: "))
total=0
for i in range(1,p+1):
    if i %2 == 0:
        total += i
print(f"The sum of even numbers between 1 and {p} is {total}")  
