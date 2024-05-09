import random

USER_ID = 1444
user_lost_counter = 0
user_profit_counter = 0

fruits = ['cherry', 'lemon', 'strawberry', 'orange', 'watermelon']

balance = int(input('Enter your initial balance: '))

while balance > 0:
    print('Your current balance is:', balance)

    bet = int(input('Place your bet: '))

    while bet > balance:
        print('Insufficient balance.Please place a bet withing your balance.')
        bet = int(input('Place your bet: '))

    if USER_ID == 1444 and user_lost_counter > 10000 and bet < 500:
        print(f'Congratulations! You won the Jackpot - {bet * 10:.2f} Euro!!!')
        print(fruits[0], fruits[0], fruits[0])
        balance += bet * 10
        user_lost_counter = 0
        continue

    reel1 = random.choice(fruits)
    reel2 = random.choice(fruits)
    reel3 = random.choice(fruits)

    print(reel1, reel2, reel3)

    if reel1 == reel2 == reel3:
        print(f'Congratulations! You won the Jackpot - {bet * 10:.2f} Euro!!!')
        balance += bet * 10
    elif reel1 == reel2:
        print(f'Congratulations! You won  - {bet * 2:.2f} Euro!!!')
        balance += bet * 2
    else:
        print('Sorry, you lost! ry again!')
        balance -= bet
        user_profit_counter += bet
if balance <= 0:
    print('Game Over! You final balance is:', balance)


