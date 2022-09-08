import math

minute = 5
arg = "Argument"

#s = "Sorry is this the {} minute {}?". format(5, "Argument") #or
s = f"Sorry is this the {5} minute {'Argument'}?"
#s = f"Sorry is this the {minute=} minute {'Argument='}?"

print("{:^10} is {:.2e} years old".format("Bill", math.pi * 100))
print(s)

for i in range(1, 11):
    sym = '*' * i
    print('{:10}'.format((sym)))#or
    #print(f'{sym:>10}')