# Where you want to dynamically generate some texts with your variables
first_name = 'Being'
second__name = 'Jay'
message = (first_name + ' [' + second__name + '] ' 'is a coder')
# formatting the above line 4 by prefixing f in the start and
# using curly braces to dynamically insert values in your strings
msg = f'{first_name} {second__name} is a coder'
print(msg)
print(message)
