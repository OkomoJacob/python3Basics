""""
List methods is also called list functions
They are some of the operations we can perform in a list e.g add new item, eliminate, search existance of an
item in the list
e.g
list.append()
list.sort()
list.insert(index, object)
list.clear() clear all in te list
list.remove(object)
list.index(object): Checks the 1st occurance of the itemin a list and displays its index
list.pop() ==removes the last object/item in the list or only prints that single object
"""

numbers = [3, 5, 6, 7, 8, 9, 89]
# numbers.index(4)
print(56 in numbers)
# >>> False and it is safer

numbers = [3, 77, 7, 8, 9, 5, 6, 89]
print("Original :" , numbers)
numbers.sort()

print("Sorted :" , numbers)
numbers.append(89090)
print(numbers)

# >>>4
numbers = [3, 5, 6, 7, 8, 9, 89]
print(numbers.sort())

# >>>None
numbers = [3, 5, 6, 7, 8, 9, 89]
numbers.sort()
print(numbers)
# >>>[3, 5, 6, 7, 8, 9, 89]

numbers = [3, 5, 6, 7, 8, 9, 89]
numbers.sort()
numbers.reverse()
print(numbers)

# >>>[89, 9, 8, 7, 6, 5, 3]
numbers = [3, 5, 6, 7, 8, 9, 89]
numbers_1 = numbers.copy()
print(numbers_1)
