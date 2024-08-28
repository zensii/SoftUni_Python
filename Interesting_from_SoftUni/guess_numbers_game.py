import random

# set the number range
min_number = 1
max_number = 100

secret_number = random.randint(min_number, max_number)
guesses = 7

print(f'I"m thinking of a number between {min_number} and {max_number}. You have {guesses} to find it.')

for guess_count in range(1, guesses + 1):

    while True:
        try:
            guess = int(input('Guess a number: '))
            if guess < min_number or guess > max_number:
                print(f'Invalid guess. Please enter a number between {min_number} and {max_number}.')
            else:
                break
        except ValueError:
            print('Invalid input. Please enter a number.')

    if guess == secret_number:
        print(f'Congratulations! You have guessed the number in {guess_count} guesses.')
        break
    elif guess < secret_number:
        print('Too low. Try Again.')
    else:
        print('Too high. Try Again.')

if guess_count == guesses:
    print(f'Sorry, you ran out of guesses. The secret number was {secret_number}.')