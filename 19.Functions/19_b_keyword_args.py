# Parameter is a placeholders that we define in our fnct to receeive the info
# while argument is the actual piece of info that you feed into your function
# Keyword args is when you assign parameter value followed by its value with an equal sign as shown below
# kwargs are good to increase the readability of your code and very suitable for numerical functions
# NB whn mixing both positional and kwargs, posargs should come 1st followed by kwargs later(in the same line)
def greet_user(first_name, last_name): #name in the parameter
    print('Hi {} {}!'.format(first_name, last_name))
    print('Welcome aboard')


print("start")
greet_user(last_name = "Smith", first_name = "John")
print("Finish")