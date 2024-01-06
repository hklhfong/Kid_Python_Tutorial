import random
import time

def generate_random_string(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-+=<>? "
    return ''.join(random.choice(characters) for _ in range(length))

def typing_game():
    print("Welcome to the Keyboard Typing Game!")
    print("Type the following text as fast as you can:")
    
    target_text = generate_random_string(20)  # Adjust the length of the string as needed
    print(target_text)

    input("Press Enter when you are ready to start typing...")
    
    start_time = time.time()
    user_input = input("Start typing here: ")
    end_time = time.time()

    elapsed_time = end_time - start_time

    # Calculate words per minute (WPM)
    words_per_minute = len(user_input.split()) / (elapsed_time / 60)

    print(f"\nTime: {elapsed_time:.2f} seconds")
    print(f"Words per Minute (WPM): {words_per_minute:.2f}")

if __name__ == "__main__":
    typing_game()
