# METHODS

course = "I'm learning python on my own"
# .upper takes no arguments.
print(course.upper())
# if we need to find the index of the first occurance of that given character in a string.
# we call the find() command.
# find is case sensitive as well
print(course.find('O'))  # if there is none it will return -1

# Maybe we want to replace a string.

msg = 'Python for beginners'
# the replace is very much case sensitive and only replaces the exact word(character)
print(msg.replace('for beginners', 'is the sweetest programming language'))

# To check the existance of a word in a string
# We use the in operator
# Again this is case sensitive and will search exact character
# The 'in' operator uses the boolean method to decide while the find uses index to decide.
word = 'I love python and web design'
print('love' in word)

# word.title() takes no arguments and capitalizes the first characters in the srting
print(word.title())
