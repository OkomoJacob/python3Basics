# inputs in the console are by default strings so you need to type cast before you can dynamically manipulate ints or floats
year_birth = input('Year of birth: ')
print(type(year_birth))
age = 2019 - int(year_birth)
print(type(age))
print(age)
