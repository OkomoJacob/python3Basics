from utils import find_max

list_x = input("Enter a list of numbers: \n -> ")
list_x = list_x.split()
# assume that list_x
#[0] is the largest...LOL!

print(f'Our list is: {list_x}')
print(f'The largest number in our list is: {find_max(list_x)}')
