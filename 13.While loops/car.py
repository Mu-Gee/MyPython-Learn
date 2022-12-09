# Car game using the while loop
command = ""
started = False
while True:
    # Here we avoid DRY by converting all the inputs to lowercase
    command = input(">").lower()
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print('''
        start - start the car
        stop  - stop the car
        quit  - quit
        ''')
    elif command == "quit":
        break
    else:
        print("Sorry, I do not understand that")
