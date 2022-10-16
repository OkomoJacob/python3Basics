temperature = 30
if temperature > 30:
    print("It's a hot day")

elif temperature < 10:
    print("It's a cold day")

else:
    print("It's neither hot nor cold")

name = input(print("Enter your name: "))

if len(name) < 3:
    print("Name MUST be at least 3 Characters!")
elif len(name) > 50:
    print("Name MUST be at most 50 characters!")
else:
    print("Name looks good!")
