# cont = []
#
# for i in range(1, 11):
#     cont.append(i)
#print(count)

# squares = []
#
# for i in range(1, 11):
#     squares.append(i ** 2)
#print(squares)
cont = [num for num in range(1, 11)]
squares = [num **2 for num in range (1, 11)]
evens = [even for even in range(1, 11) if even % 2 == 0]
even_squared_odd_cubed = [num ** 2 if num % 2 ==0 else num ** 3 for num in range(1, 11)]
print(even_squared_odd_cubed)
print(evens)
print(cont)
print(squares)

names = ['bimpe', 'Banke', 'abimbola', 'Kelechi', 'James', 'Olalekan', 'Racheal']
my_names = [name for name in names if name.istitle()]
#input_names = [input("Name? ") for _ in range(5)]

input_names = [input(f"{i + 1}.Name? ") for i in range(5)]
# my_names = []
# for name in names:
#     if name.istitle():
#         my_names.append(name)
#print(my_names)
print(input_names)
x_and_y = []
for x in range(1,6):
    for y in range(1,6):
        x_and_y.append((x,y))

# x_and_y = [(x, y) for x in range (1, 6) for y in range(1, 6)]
print(x_and_y)

listcomp = [num % 3 for num in range(1, 10)]
setcomp = [num % 3 for num in range(1, 10)]
dictcomp = {k:v for k, v in enumerate(range(11, 16), 11)}
genexp = (num for num in range(1, 6))

print(type(listcomp), listcomp)
print(type(setcomp), setcomp)
print(type(dictcomp), dictcomp)
print(type(genexp), genexp)