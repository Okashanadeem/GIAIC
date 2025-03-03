import random

def computer_guesses():
    print("Think of a number between 1 and 100, and I'll try to guess it!")
    low, high = 1, 100
    attempts = 0
    
    while True:
        guess = random.randint(low, high)
        attempts += 1
        
        print(f"Is your number {guess}? (Enter 'h' for too high, 'l' for too low, 'c' for correct)")
        feedback = input().lower()
        
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback == 'c':
            print(f"Yay! I guessed your number in {attempts} attempts!")
            break
        else:
            print("Invalid input. Please enter 'h', 'l', or 'c'.")

computer_guesses()
