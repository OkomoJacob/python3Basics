# Parameter is a placeholders that we define in our fnct to receeive the info
# while argument is the actual piece of info that you feed into your function
# Here i've used positional arguments(unkike key word arguments) meaning the position and order of the args really matter
def greet_user(first_name, last_name): #name in the parameter
    print('Hi {} {}!'.format(first_name, last_name))
    print('Welcome aboard')


print("start")
greet_user("John", "Smith") #john and mary are the argumnets
greet_user("Mary", "Stephanie")
print("Finish")