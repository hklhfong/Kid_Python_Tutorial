class NumberGuessingGame:
    def __init__(self, min_range, max_range):
        self.min_range = min_range
        self.max_range = max_range
        self.secret_number = None
        self.attempts = 0

    def start_game(self):
        print("Welcome to the Number Guessing Game!")
        print(f"I'm thinking of a number between {self.min_range} and {self.max_range}. Can you guess it?")

        # Generate a secret number
        self.secret_number = 42  # You can change this to a random number within the range

        while True:
            guess = int(input("Enter your guess: "))
            self.attempts += 1

            if guess == self.secret_number:
                print(f"Congratulations! You guessed the number {self.secret_number} in {self.attempts} attempts.")
                break
            elif guess < self.secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")

if __name__ == "__main__":
    # Create an instance of the NumberGuessingGame class
    game = NumberGuessingGame(min_range=1, max_range=100)

    # Start the game
    game.start_game()
