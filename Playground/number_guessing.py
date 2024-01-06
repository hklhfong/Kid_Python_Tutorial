import random
import time

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

def generate_random_number():
    return random.randint(1, 100)  # Generates a random number between 1 and 100


def get_player_guess():
    while True:
        try:
            guess = int(input("Guess the number between 1 and 100: "))
            return guess
        except ValueError:
            print_slow("Invalid input! Please enter a number.")


def number_guessing_game():
    random_number = generate_random_number()
    attempts = 0

    print_slow("Welcome to the Number Guessing Game!")
    print_slow("I'm thinking of a number between 1 and 100.")

    while True:
        player_guess = get_player_guess()
        attempts += 1

        if player_guess < random_number:
            print_slow("Too low! Try again.")
        elif player_guess > random_number:
            print_slow("Too high! Try again.")
        else:
            print_slow(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

if __name__ == "__main__":
    # Here's where we put all our game code. When we click "Start" (by running the program),
    # the computer starts reading the code from here. It's like magic!
    
    # So, everything inside this block is part of our game, and the fun begins!
    number_guessing_game()
