'''
Try running the code and anticipate for the errors and
 when a ValueError is encountered, catch it with an exception message properly
'''
try:
    age = int(input('Enter age: '))
    print(age)
except ValueError: #Catch the error
    print('Invalid input, Integers only')
try:
    age = int(input('Enter age: '))
    income = 300
    risk = income / age
    
except ZeroDivisionError: #Catch the error
    print('Invalid input, Cannot divide number by Zero')
