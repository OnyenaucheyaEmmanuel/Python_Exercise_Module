word = (input("Enter a word : "))

if word[::-1] == word[::1]:
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")

s = "hello world!"
print(len(s))

t = 3 * s
print(t)

y = "t" in s
print(y)

new_s = "L" + s[11:]
print(new_s)
print(help(s.find))
print(s.upper())
print(s.lower())
name = "Timilehin Ade"
print(name.lower())

print(name.title())

print(name.capitalize())

print(name.upper())

print(name.casefold())

print(name.swapcase())

print(name.startswith("T"))

print(name.startswith("Timilehi"))

print(name.startswith("Timilehin".upper()))

print(name.ljust(20))

print(name.rjust(20))

print(name.center(20))

print(name.center(20, '@'))

for i in range(1, 21, 2):
    print(('*' * i).center(20))

for i in range(1,11):
    print('*' * i)

for i in range(1, 11):
    print(('*' * i).rjust(10))

for i in range(1,21):
    print(('*' * i).ljust(10))

print(name.count('e'))

print((name.find('n')))

print((name.find('z')))

print((name.index('h')))

print(name.find('imi'))

print(name.replace('Ade', 'Mayo'))

print((name.replace('T', '$')))

print((name.replace('i', '*', 1)))

binary = "1011001001"
print(((binary.replace("1", "#"))).replace("0", "1").replace("#", "0"))

print((binary.translate(str.maketrans("01", "10"))))

print((name.translate(str.maketrans("i", "@"))))

j = "12301203450123"
print((j.translate(str.maketrans('012', '109', '3')))) #replace 0 with 1, 1 with 0 and 2 with 9, and also remove 3





