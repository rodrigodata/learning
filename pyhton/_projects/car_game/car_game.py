# command
## start - start the car
## stop - stop the car
## exit -- terminate the program
program_is_running = True
car_is_on = False
car_is_offline = True

while program_is_running:
    command = input('> ').upper()

    if command == 'START' and car_is_on == False and car_is_offline == True:
        car_is_offline = False
        car_is_on = True
        print('Car started...Ready to got!')
    # car already started
    elif command == 'START' and (car_is_on == True or car_is_offline == False):
        print('It seems your car is already started...')
    # car already stopped
    elif command == 'STOP' and (car_is_on == False or car_is_offline == True):
        print('It seems your car is already stopped...')
    elif command == 'STOP' and car_is_on == True and car_is_offline == False:
        car_is_offline = True
        car_is_on = False
        print('Car stopped.')
    elif command == 'HELP':
        print("""
        start - start your car
        stop - stop your car
        quit - quit game
        """)
    elif command == 'QUIT':
        break
    else:
        print("I don't understand that...")
        
