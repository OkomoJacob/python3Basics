"""To find the largest number in a list, you'll need the list array and
 assume that the first number in the list(index [0] is probably the largest.
 Then create a for loop to iterate through all the numbers to find the largest of all
"""

list_x = [3, 5.78, 789, 94, 800, 894, 985, 9, -90.489]
# assume that list_x[0] is the largest...LOL!
Max = list_x[0]
for num in list_x:
    if num > Max:
        Max = num
print(f'Our list is: {list_x}')
print(f'The largest number in our list is: {Max}')
