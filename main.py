import random

def play_game():
    random_number = random.randint(1,10)
    attempts = 0

    while True:
        user_guess = int(input('Guess your number between 1 and 100: '))
        attempts += 1

        
        if user_guess == random_number:
            print('congratulations you guessed correctly!!!')
            break

        elif user_guess < random_number:
            print('Sorry, Too Low, Guess a higher number')

        else:
            print('Sorry, Too high, guess again')
