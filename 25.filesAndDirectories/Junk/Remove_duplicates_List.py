"""
This program will remove duplicates from a list using list methods
"""
nums = [2, 6, 34, 56, 90, 56, 56, 45, 23, 55, 5, 88, 90]
uniques = []
for i in nums:
    if i not in uniques:
        uniques.append(i)
        uniques.sort()
print(uniques)
