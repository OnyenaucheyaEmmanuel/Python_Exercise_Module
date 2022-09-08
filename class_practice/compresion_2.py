listcomp = [num % 3 for num in range(1, 10)]
setcomp = [num % 3 for num in range(1, 10)]
dictcomp = {k:v for k, v in enumerate(range(11, 16), 11)}
genexp = (num for num in range(1, 6))

print(type(listcomp), listcomp)
print(type(setcomp), setcomp)
print(type(dictcomp), dictcomp)
print(type(genexp), genexp)

print(next(genexp))
print(list(genexp))

print([i for i in range(10_000_000_000)])
