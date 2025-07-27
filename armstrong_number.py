
n = int(input("enter a number"))

digits= len(str(n))
temp = n
result = 0

while temp > 0 :
    digit = temp % 10
    result  += digit ** digits
    temp //= 10

if result == n :
    print(f"{n} is a armstrong number")
else: 
    print(f"{n} is not armstrong number")