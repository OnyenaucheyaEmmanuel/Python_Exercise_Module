# import random
#
# lst = list(range(1, 11))
# print(lst)
# random.shuffle(lst)
#
#
# print(lst)
# #print(random.choice(lst)
#
# lst.append(20)
# print(lst)
#
# #lst.append([20, 30, 40])
# #lst.extend([20, 30, 40])
# lst += [20,30,40]
#
# lst.insert(-3, 56)
# print(lst)
#
# last_item = lst.pop()
# print(last_item)
#
# item_at_inde_0 = lst.pop(0)
# print(item_at_inde_0)
#
# print(lst)
#
# print("Count", lst.count(5))
# lst.remove(8)
# print(lst)
#
#
# #lst.clear()
#
# l = [1, 2, [3,4], 5]
# l2 = l.copy()
#
# #l1.append(6)
# #print(l2)
#
# l2[2].append(7)
# print(l1)
#
# print(lst.index(3))
#
#
# s = "write a sentence and reverse it"
# s_list = s.split()
# s_list.reverse()
# print(" " )
#
# lst.sort(reverse=True)
# print(lst)

def last_elem(string):
    return string[-1]

fruits = ["banana","apple", "cucumber", "mango", "grape"]
fruits.sort(key= last_elem)
print(fruits)
fruits.sort(key= last_elem, reverse=True)
print(fruits)


lst = [3,-1,5,4], 3

def two_sum (arr:list, target:int) -> list:
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
    return [-1, -1]
arr = [3,-1,5,4]
target = 3
print(two_sum(arr,target))

def balance_pair(brackets: str)-> bool:
    if brackets.strip() == "" or len(brackets) % 2 == 1:
    #if not brackets or len(brackets) % 2 ==1:
        return False
    # else:
    #     return True


#print(balance_pair("[]"))
    stack: list = []

    for bracket in brackets:
        if bracket in "{[(":
            stack.append(bracket)
        elif bracket in "}])":
            peek: str = stack[-1]
            if peek == "{" and bracket == "}":
                stack.pop()
            elif peek == "[" and bracket == "]":
                stack.pop()
            elif peek == "(" and bracket == ")":
                stack.pop()
            else:
                return False
        else:
            return False

        return True
print(balance_pair("{[("))

tup = (1,2,3,[4,5,6],7)
print(tup)

tup[3][1] = 100
print(tup)



a_str = 'He had the bat'
print(a_str.find('t', a_str.find('t') + 1))

print("i am " + '29'+ ' years old')
#
# spam = input()
# y = int(spam)
# print(y * 10/5)

name = "mAry"
password = 'swordfish'
if name == 'mary':
    print('Hello Mary')
if password == 'swordfish':
    print('Access granted.')
else:
    print('Wrong password')



