'''
EXERCISE: Write a code to ask for integers and convert them into strings
'''
phone = (input('Enter a phone number:'))

key_values = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five",
    "6" : "Six",
    "7" : "Seven",
    "8" : "Eight",
    "9" : "Nine",
    "0" : "Zero"  
}
# Loop through the phone string and check
output = ""
for phone_dig in phone:
    output += key_values.get(phone_dig, "!") + " "
print(output)

