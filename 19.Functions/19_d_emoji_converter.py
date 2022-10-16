def emoji_converter(message):
    words = message.split(' ')

    # Define a dict to map the characters into emojis
    emojis = {
        ":)" : "happy",
        ":(" : "sad"
    }
    # Loop through the words and potentially map in into an emoji
    # Set output into an empty string
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output

    
message = input("Enter message : -> ")
# To split the message in the terminal and display it as a list
print(emoji_converter(message))