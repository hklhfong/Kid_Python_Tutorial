import time

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

def make_choice(question, options):
    while True:
        print_slow(question)
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")
        
        choice = input("Enter the number of your choice: ")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(options):
                return choice
        print("Invalid choice. Please enter a valid number.")

def play_story():
    print_slow("Once upon a time, in a magical land...")
    print_slow("You are a brave adventurer on a quest to find a hidden treasure.")
    
    choice1 = make_choice("You come across a fork in the road. Which way will you go?", ["Take the left path.", "Take the right path."])
    if choice1 == 1:
        print_slow("You chose the left path and found a chest filled with gold coins! Well done!")
    else:
        print_slow("You chose the right path and found yourself facing a friendly dragon. The dragon offers to help you on your quest.")
        choice2 = make_choice("What will you do?", ["Accept the dragon's help.", "Decline the dragon's help."])
        if choice2 == 1:
            print_slow("The dragon becomes your trusty companion and together you find the hidden treasure.")
        else:
            print_slow("You continue your quest on your own and eventually find the hidden treasure.")

    print_slow("You have successfully completed your adventure and found the hidden treasure. You are a hero!")

if __name__ == "__main__":
    play_story()
