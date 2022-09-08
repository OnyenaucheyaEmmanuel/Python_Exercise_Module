number = int(input("Enter Number to find factorial : "))

fact = 1
for count in range(1, number +1):
    fact = fact * count
print("The Factorial of", number, "is", fact)
