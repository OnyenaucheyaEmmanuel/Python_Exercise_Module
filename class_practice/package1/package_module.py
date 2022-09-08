# def add(a: float, b: float) -> float | None:
#      try:
#          return a/b
#      except:
#          print("Can't divide with zero")
#          return None
#
#
# print(add(1, 0))
#
# def add(a: float, b: float) -> float | None:
#     try :
#         #c = a + 'b'
#         #name = int('great')
#         lst = [1, 2, 3]
#         #print(lst[6])
#         file = open('file.txt', mode='r', encoding='utf-8')
#         print(file.read())
#         print("About to close")
#         file.close()
#         return a / b
#     except ZeroDivisionError:
#         print("Can't divide with zero")
#         return None
#     except (TypeError, NameError):
#         print("Type error")
#
# print(add(1, 0))

cheeses = ['Cheddar', 'Edam', 'Gouda']
numbers = [17, 123]
empty = []
print(cheeses, numbers, empty)

import pathlib

path = pathlib.Path.home()/"hello.txt"
print(path)
print(list(path.parents))

for directory in path.parents:
    print(directory)

print(path.anchor)
# path = pathlib.path("hello.txt")
# print(path.anchor)
home = pathlib.Path.home()
print(home.name)

path = home / "hello.txt"
print(path.name)

path = pathlib.Path.home() / "hello.txt"
print(path.stem)
print(path.suffix)

