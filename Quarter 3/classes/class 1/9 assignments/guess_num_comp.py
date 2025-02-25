import random

def guess_num(x):
    random_num = random.randint(1,x)
    guess = 0
    while guess != random_num:
        guess = int(input(f"Guess a number! between 1 to {x} \n"))
        if guess > random_num:
            print("Sorry. It's too high. Try again.")
        elif guess < random_num:
            print("Sorry. It's too low. Try again.")
    print(f"Congratulation! you've guessed the number {random_num} correctly!")

guess_num(20)