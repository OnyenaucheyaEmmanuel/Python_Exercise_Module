import random

def add(a:int, b: int)->int:
    """add two numbers"""
    return a + b

print(add.__name__)
print(add.__doc__)
print(add.__annotations__)

def operate(x, y,func):
    return func(x, y)

print(operate(2,3, add))

def sub(x, y):
    return y - x

print(operate(2,3, sub))

def multiply(a):
    def by(b):
        return  a*b
    return by

multiply_by_five = multiply(5)

print(multiply_by_five(6))

add = lambda a, b: a + b
print(add(10, 9))
print(operate(2,3,lambda a, b: b-a))
print(operate(2,3,lambda a, b: b+a))
print(operate(2,3,lambda w, y: w*y))

#import builtins
# sum = 67
# print(builtins.sum([1,2,3]))
# print(dir(builtins))
print(round(5636.6754, -4))

# import builtins
arr = [1,6,4,7,2]
print(sum(arr, 100))

letters = [['a'], ['b', 'c'], ['d'], ['e', 'f']]
print(sum(letters, []))

print(min([1,2,3,4,5,6]))

fruits = "apple pear  cucumber mango grape melon".split()
print(max(fruits, key=len))
print(min(fruits, key=len))
print(max(fruits, key=lambda x:x[-1]))

print(max(fruits, key=lambda x:x[-3:]))

def last_three(x):
    return x[-3:]

print(max(fruits, key=last_three))

users = [
    {
        'name': 'Hadiza',
     'age': 21,
     'gender': 'Female',
     'user_name': 'deezah',
     'is_verified': True,
     'tweets': [
         {'contents': 'PO for President', 'likes': 450, 'retweets': 233},
         {'contents': 'Atiku nis our man', 'likes': 4, 'retweets': 2},
                ]
     },
        {
        'name': 'Ibrahim',
     'age': 32,
     'gender': 'Male',
     'user_name': 'ibro',
     'is_verified': True,
     'tweets': [
         {'contents': 'Programming is fun', 'likes': 34, 'retweets': 12},
                ]
     },
        {
        'name': 'James',
     'age': 25,
     'gender': 'Male',
     'user_name': 'ames',
     'is_verified': True,
     'tweets': [
         {'contents': 'Love is life', 'likes': 450, 'retweets': 233},
         {'contents': 'Only Racheal I kmow', 'likes': 4, 'retweets': 2},
                ]
     },
        {
        'name': 'Racheal',
     'age': 21,
     'gender': 'Female',
     'user_name': 'betty',
     'is_verified': False,
     'tweets': [
         {'contents': '.', 'likes': 1450, 'retweets': 1330},
         {'contents': 'Thinking about ames', 'likes': 4, 'retweets': 2},
         {'contents': 'Amazing grace', 'likes': 2000, 'retweets': 10000},
                ]
     },
        {
        'name': 'Elijah',
     'age': 17,
     'gender': 'Male',
     'user_name': 'el_di_si',
     'is_verified': False,
     'tweets': [
         {'contents': '.', 'likes': 1450, 'retweets': 1330},
         {'contents': 'Thinking about ames', 'likes': 4, 'retweets': 2},
                ]
     },
        {
        'name': 'Dorris',
     'age': 16,
     'gender': 'Female',
     'user_name': 'anything',
     'is_verified': False,
     'tweets': [
         {'contents': 'I love Chimamanda', 'likes': 1450, 'retweets': 1330},
         {'contents': 'Feminism is the goal', 'likes': 45, 'retweets': 67},
                ]
     },
        {
        'name': 'Jacob',
     'age': 37,
     'gender': 'Male',
     'user_name': 'elder',
     'is_verified': True,
     'tweets': [
         {'contents': 'Reflection is my goal', 'likes': 50, 'retweets': 13},
         {'contents': 'How to get more likes on twitter', 'likes': 1, 'retweets': 5},
                ]
     },
        {
        'name': 'Derrick',
     'age': 29,
     'gender': 'Male',
     'user_name': 'standby_gen',
     'is_verified': False,
     'tweets': [
                ]
     },
{
        'name': 'Mubarak',
     'age': 47,
     'gender': 'Male',
     'user_name': 'whistle',
     'is_verified': True,
     'tweets': [
                ]
     },

]

print(max(users, key=lambda  x: x['age']))
print(max(users, key=lambda  x: len(x['tweets'])))


iterate1 = (1,2,3,4)
iterate2 = ('hello', 'how', 'are', 'you')
print(list(zip(iterate2, iterate1, strict=True)))#to resist it
print(dict(zip(iterate2, iterate1)))
print(sorted('helloAZ', reverse=True))
print(sorted(fruits, reverse=True))
print(sorted(fruits, key=len))
print(sorted(fruits, key=lambda x : x[-1]))

print(max([user['age'] for user in users]))

print(sum([user['age'] for user in users])/ len(users))

print(any(user['is_verified'] for user in users))
print(all(user['is_verified'] for user in users))

lst = [1,2,3,4,5]
print(list( map(lambda  x: x ** 2, lst)))#map
print(([x **2 for x in lst]))#list comprehension

print((list(map(str.upper, fruits))))
print((list(map(lambda  x: x.upper(), fruits))))
fruits.append('Agbado')
print(list(map(str.istitle, fruits)))
print(list(filter(str.istitle, fruits)))
print(list(filter(lambda x: not x.istitle(), fruits)))
print(list(map(lambda y: y.upper(), filter(lambda x: not x.istitle(), fruits))))
print([x.upper() for x in fruits if not x.istitle()])

#import adder
#
# value = adder.add(2,2)
# print(value)
# #
# def add(x, y):
#     return x + y

#
# from functools import reduce
#
# def reduce_func(acc, item):
#     print(f"acc-> {acc} <> item -> {item}")
#     return acc * item
#
# from math import prod
# print("\n############ Reduce ##############\n")
# #print(reduce(lambda acc, item: acc + item, lst))
# random.shuffle(lst)
# print(lst)
# print(reduce(reduce_func, lst))
# print(prod(lst, start=100))
# fruits.append("lettuces")
# print(reduce(lambda acc, item: acc if acc > item else item, lst))
# print(reduce(lambda acc, item: acc if len(acc) > len(item) else item, fruits))
# print(reduce(max_func, fruits))
# print(max(lst))
#print("\n############ Reduce ##############\n")
#print(reduce(lambda acc, item: acc + item, lst))
# print(lst)
# print(reduce(reduce_func, lst))
# print(sum(lst, 100))

print("####### match ########")

#num = int(input("Enter a number: "))

# match num:
#     case 1:
#         print(1)
#     case 2:
#         print(2)
#     case _:
#         print("Don't know you")

# match num:
#     case _ as x if 1 <= x <= 10:
#         print(x)
#     case _ as x if 11 <= x <= 20:
#         print(x)
#     case 30 | 40 | 50:
#         print(x)
#     case _:
#         print("Don't know you")



# lst = [20, 13, 16]
#
# match lst:
#     case [i1, i2, i3]:
#         print(i3, i2, i1)
#     case _:
#         print("Nothing match")
lst = [20, 13, "good"]

match lst:
    case [i1, i2, int(i3)]:
        print(i3, i2, i1)
    case _:
        print("Nothing match")

d = {
    "name": "Hadiza",
    "age": 18,
    "is swit": True
}
match d:
    case {"name": str(name), "age": int(age)}:
        print(name, age)
    case _:
        print("nothing to match")

def fizzbuzz(num):
    three = num % 3
    five = num % 5
    match (three, five):
        case (0, 0):
            return "FIZZBUZZ"
        case (0, _):
            return "FIZZ"
        case (_, 0):
            return "BUZZ"
        case _:
            return num

for i in range(1, 10):
    print(fizzbuzz(i))

def suming_list(list_: list[int]) -> int | None:
    match list_:
        case []:
            return 0
        case [first_value, * another_list]:
            return first_value + suming_list(another_list)
        case _:
            print("Can only accept an int")
            return None

import itertools

print(suming_list([1,2,3,4,5]))
print(list(itertools.zip_longest([1,2,7,9], [3, 4, 5, 6, 4], fillvalue=0))) #mapping

print(4 ** 9)




