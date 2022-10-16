"""To find the largest number in a list, you'll need the list array and
 assume that the first number in the list(index [0] is probably the largest.
 Then create a for loop to iterate through all the numbers to find the largest of all
"""

def find_max(list_x):
    Max = list_x[0]
    for num in list_x:
        if num > Max:
            Max = num
    return Max
  