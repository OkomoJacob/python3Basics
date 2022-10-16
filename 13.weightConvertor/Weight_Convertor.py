weight = float(input("Enter weight: "))

choice = input("M(Mass) or (K)Kg: ")

if choice.upper() == 'M':
    converted = weight / 1000
    print(f"You are {converted} Kgs")

elif choice.upper() == 'K':
    converted = weight * 1000
    print(f"You are {converted} gramms")

else:
    print("Wrong input!")
