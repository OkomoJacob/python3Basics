""""
If we need to input very many commands, we set our initial string to be empty as in line 3
While loops are used to execute a block of code multiple times.
"""
print("Type 'help' for User guide")
command = ""
___started = False
while True:
    
    command = input("-> ").lower()
    if command == 'start':
        if ___started:
            print("Car has already started!")
        else:
            ___started = True
            print("Car has started...")

    elif command == 'stop':
        if not ___started:
            print("Car has already stopped!")
        else:
            ___started = False
            print("Car stopped.")
    elif command == "help":
        print("""
    start - To start car...
    stop - to stop car
    q - to exit game
        """)
    elif command == 'q':
        break
    else:
        print("Sorry that is not a recognized command!, type 'help' for user guide")
