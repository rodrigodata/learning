secret_number = 10
guesses = 0

while guesses < 3:
    guess = int(input('Guess: '))
    guesses += 1
    if secret_number == guess:
        print('You won!')
        break
else:
    print('Sorry you failed!')